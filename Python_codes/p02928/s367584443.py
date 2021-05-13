N, K = map(int,input().split())
A = list(map(int,input().split()))

mod = 10**9 + 7

right_numbers = [0]*N
left_numbers = [0]*N
right_ans = [0]*N
left_ans = [0]*N

right_total = K*(K+1)//2
left_total = K*(K-1)//2

for i in range(N):
    for r in range(i+1,N):
        if A[i] > A[r]:
            right_numbers[i] += 1
    for l in range(0,i):
        if A[i] > A[l]:
            left_numbers[i] += 1
    #print(right_numbers[i] * right_total)
    #print(left_numbers[i] * left_total)
    right_ans[i] = right_numbers[i] * right_total
    left_ans[i] = left_numbers[i] * left_total

"""
print(right_numbers)
print(left_numbers)
print(right_ans)
print(left_ans)
print(sum(right_ans))
print(sum(left_ans))
"""
print((sum(right_ans) + sum(left_ans)) % mod)