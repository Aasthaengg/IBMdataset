N = input()
A = map(int,raw_input().split())

flag = 1
x = 0
while flag:
    flag = 0
    for i in range(1,N):
        j = N - i
        if A[j] < A[j-1]:
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
            x += 1
            flag = 1

for i in range(N-1):
    print A[i],
print A[-1]

print x