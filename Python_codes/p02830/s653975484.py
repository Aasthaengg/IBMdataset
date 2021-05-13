n=int(input())

x,y = map(str,input().split())

ans = ''

for i in range(n):
    ans = ans + x[i] + y[i]
print(ans)