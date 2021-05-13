n = int(input())
A = input().split(' ')
count = 0

flag = True
while flag:
    flag = False
    for j in reversed(range(1, n)):
        if int(A[j]) < int(A[j-1]):
            (A[j-1], A[j]) = (A[j], A[j-1])
            count += 1
            flag = True

print(" ".join(A))
print(count)