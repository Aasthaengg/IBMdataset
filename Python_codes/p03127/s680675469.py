n = int(input())
A = sorted(list(map(int, input().split())))

while len(A) > 1:
    A = sorted([i%A[0] for i in A if i%A[0]!=0] + [A[0]])
print(A[0])