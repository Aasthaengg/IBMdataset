N, M = map(int, input().split())
A = set(list(map(int, input().split()))[1:])
for i in range(1, N):
    A = A & set(list(map(int, input().split()))[1:])
print(len(A))