s = input()
k = int(input())

A = []
for i in range(1, 6):
    for j in range(len(s)-i+1):
        A.append(s[j:j+i])


A = sorted(set(A))

print(A[k-1])
