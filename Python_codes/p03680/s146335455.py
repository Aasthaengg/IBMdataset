n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

b = [True]*n
btn = 1
ans = 0
while b[btn - 1]:
    ans += 1
    b[btn - 1] = False
    btn = A[btn - 1]
    if btn == 2:
        b[1] = False
        print(ans)
        break
if b[1]:
    print(-1)
