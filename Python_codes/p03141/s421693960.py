n = int(input())
ans = 0
cou = []
for i in range(n):
    a , b = map(int,input().split())
    ans += a
    cou.append(a+b)
cou.sort(reverse=True)
for i in range(1,n,2):
    ans -= cou[i]
print(ans)