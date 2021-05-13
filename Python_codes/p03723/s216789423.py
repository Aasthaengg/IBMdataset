a,b,c = map(int,input().split())
if a == b == c:
    if a % 2 == 0:
        print(-1)
        exit(0)
    else:
        print(0)
        exit(0)
ans = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    al = b // 2 + c // 2
    bl = a // 2 + c // 2
    cl = a // 2 + b // 2
    a = al
    b = bl
    c = cl
    ans += 1
print(ans)