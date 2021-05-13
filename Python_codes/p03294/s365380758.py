n = int(input())
A = list(map(int, input().split()))
ans = [A[i]-1 for i in range(len(A))]

print(sum(ans))