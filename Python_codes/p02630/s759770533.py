N = int(input())
A = list(map(int,input().split()))

nums = [0 for i in range(1,100010)]

S = sum(A)
for i in range(N):
    nums[A[i]] += 1

Q = int(input())
for i in range(Q):
    B,C = map(int,input().split())
    if nums[B] != 0:
        plus = nums[B]*(C - B)
        S += plus
    print(S)
    nums[C] += nums[B]
    nums[B] = 0
