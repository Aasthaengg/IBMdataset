N = int(input())
A = list(map(int, input().split()))
answer = 0
temp = A[0]
right = 0

for i in range(N):
    if right < N - 1:
        while temp + A[right + 1] == temp ^ A[right + 1]:
            right += 1
            temp += A[right]
            if right == N - 1:
                break
        temp -= A[i]
        answer += right - i + 1
    else:
        answer += right - i + 1

print(answer)