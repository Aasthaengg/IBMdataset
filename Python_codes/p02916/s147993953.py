N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev_food = A[0] - 1
ans = 0
for i in range(N):
    curr_food = A[i] - 1
    ans += B[curr_food]
    if curr_food - 1 == prev_food:
        ans += C[prev_food]
    prev_food = curr_food
print(ans)