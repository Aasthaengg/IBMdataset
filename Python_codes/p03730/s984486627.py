a,b,c = map(int,input().split())

ans = 'NO'
r = a%b
x = 0
for i in range(100):
    x += r
    if x%b == c:
        ans = 'YES'
        break

print(ans)
