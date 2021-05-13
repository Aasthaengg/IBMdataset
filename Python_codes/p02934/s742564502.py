N = int(input())
A = list(map(int, input().split()))
lst = []

for i in range(N):
    x = 1 / A[i]
    lst.append(x)

print(1/sum(lst))