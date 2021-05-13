n = int(input())
s = [input() for i in range(n)]
a = [0]*n
for i in range(n):
    for j in range(10):
        a[i] += 10**(ord(s[i][j])-97)

a.sort()

cnt = 1
ans = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        cnt += 1
        if i == n-2:
            ans += cnt*(cnt-1)//2
            cnt = 0            
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1
print(ans)