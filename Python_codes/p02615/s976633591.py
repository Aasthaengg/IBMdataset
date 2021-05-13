N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)
a = N // 2

answer = 2*sum(sorted_A[0:a]) - sorted_A[0]

if N % 2 == 1:
    answer += sorted_A[a]

print(answer)