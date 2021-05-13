N = int(input())
A = [0] + list(map(int,input().split())) + [0]
acc = [abs(A[i] - A[i - 1]) for i in range(1, N + 2)]
su = sum(acc)
for i in range(N):  print(su - acc[i] - acc[i + 1] + abs(A[i] - A[i + 2]))