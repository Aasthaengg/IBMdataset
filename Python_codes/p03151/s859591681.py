n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    ans = -1
else:
    d = [a[i]-b[i] for i in range(n)]
    d.sort()
    
    i = 0
    s = 0
    while d[i] < 0:
        s -= d[i]
        i += 1
    
    j = 0
    tmp = 0
    while s > tmp:
        tmp += d[j-1]
        j -= 1
    ans = i-j
print(ans)