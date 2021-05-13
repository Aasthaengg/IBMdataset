a,b= [int(x) for x in input().split()]

n = b - a -1
ans = - a

for i in range(1, n+1):
    ans += i

print(ans)