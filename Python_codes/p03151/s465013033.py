N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

minus_sum = 0
plus_list = []
ans = 0
for i in range(N):
    if A[i] < B[i]:
        minus_sum += (B[i] - A[i])
        ans += 1
    elif A[i] > B[i]:
        plus_list.append(A[i] - B[i])
plus_list.sort(reverse=True)

if minus_sum == 0:
    print(0)
    exit()

i = 0
while minus_sum > 0:
    minus_sum -= plus_list[i]
    ans += 1
    i += 1

print(ans)
