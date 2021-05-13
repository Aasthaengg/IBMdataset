n = int(input())
saigo = 0
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    if saigo < a:
        saigo = a
        ans = a + b

print(ans)