n = int(input())
s = list(map(int,input().split()))
A = [i for i in s if i % 2 == 0]

count = 0
for i in range(len(A)):
    while A[i] % 2 == 0:
        A[i] = A[i]//2
        count += 1

print(count)