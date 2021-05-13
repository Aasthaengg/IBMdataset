N = int(input())
D, X = map(int, input().split())
sum = 0
for i in range(N):
    A = int(input())
    for j in range(1, D+1, A):
        sum += 1
print(X+sum)