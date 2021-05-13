import sys 

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_C = sum(A)

if sum_C < sum(B):
    print(-1)
    sys.exit()

lack_sum = 0
surplus_sum = []
count = 0

for i in range(N):
    if B[i] > A[i]:
        lack_sum = lack_sum + (B[i] - A[i])
        count = count + 1
    elif B[i] <= A[i]:
        surplus_sum.append(A[i]-B[i])

surplus_sum = sorted(surplus_sum,reverse=True)

if len(surplus_sum) == N:
    print(0)
    sys.exit()


for j in surplus_sum:
    lack_sum = lack_sum - j
    count = count + 1

    if lack_sum <= 0:
        print(count)
        sys.exit()

    

         

