N, A, B = map(int, input().split())

print(min(A, B), (A + B - N if A + B > N else 0))
