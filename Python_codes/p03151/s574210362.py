N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_a = sum(A)
sum_b = sum(B)
if sum_a < sum_b:
    # impossible
    print(-1)
    exit()

ans = 0
lack = 0
remains = []
for i in range(N):
    a = A[i]
    b = B[i]
    if a < b:
        ans += 1
        lack += b - a
    elif a > b:
        remains.append(a - b)

if ans == 0:
    # no need to change
    print(ans)
    exit()

remains.sort(reverse=True)

count = 0
while lack > 0:
    lack -= remains[count]
    count += 1

print(ans + count)
