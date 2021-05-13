N = int(input())
A = list(map(int,input().split()))
_sum = sum(A)
diff = [0]*(N-1)
cumul = 0
for i in range(N-1):
    cumul += A[i]
    diff[i] = abs(cumul - (_sum - cumul))
# print(diff)
print(min(diff))
