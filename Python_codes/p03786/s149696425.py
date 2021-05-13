N = int(input())
A = list(map(int, input().split()))

cumulative = [0]
A.sort()
for i in range(N):
    cumulative.append(cumulative[i] + A[i])
# print(A)
# print(cumulative)

for i in range(N - 1, 0, -1):
    # print(i)
    if A[i] > cumulative[i] * 2:
        print(N - i)
        break
else:
    print(N)
