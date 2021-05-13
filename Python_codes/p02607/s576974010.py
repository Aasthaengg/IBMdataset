n = int(input())
A = list(map(int, input().split()))

c = 0
for i in range(n):
    if i%2==0:
        if A[i] % 2 == 1:
            c += 1
print(c)