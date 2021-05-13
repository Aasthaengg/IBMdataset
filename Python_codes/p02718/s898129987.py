N, M = [int(i) for i in input().split(" ")]
A = [int(i) for i in input().split(" ")]

A.sort(reverse=True)
sum_voted = sum(A)

for i in range(M):
  if A[i] < sum_voted / (4 * M):
    print("No")
    exit(0)

print("Yes")
