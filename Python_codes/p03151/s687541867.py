n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()
BA = sorted(i - j for i, j in zip(A, B))

not_enough = 0
ans = 0
for ba in BA:
    if ba < 0:
        not_enough += ba
        ans += 1
    else:
        break
for ba in BA[::-1]:
    if not_enough >= 0:
        break
    not_enough += ba
    ans += 1
print(ans)
