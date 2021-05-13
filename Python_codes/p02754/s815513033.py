N, A, B = map(int, input().split())
answer = N // (A+B) * A
answer += min(N % (A + B), A)
print(answer)
