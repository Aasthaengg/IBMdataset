A, B, C = map(int, input().split())
ans = 0
while A%2 == 0 and B%2 == 0 and C%2 ==0:
    ans += 1
    a, b, c = A//2, B//2, C//2
    A = b+c
    B = a+c
    C = a+b
    if ans == 100: break
if ans == 100:
    print(-1)
else:
    print(ans)
