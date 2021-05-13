n = int(input())
a = list(map(int,input().split()))
res = 0
i = 1
while i < n+1:
    if a[i-1] == i:
        res += 1
        i+=2
    else:
        i+=1
print(res)