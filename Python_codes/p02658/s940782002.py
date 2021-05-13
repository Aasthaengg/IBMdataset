N = int(input())
I = list(map(int, input().split()))
ans = 1

kMax = 10**18

if 0 in I:
    print(0)
    exit()

for i in I:
    ans *= i
    if ans > kMax:
        print(-1)
        exit()
print(ans)

