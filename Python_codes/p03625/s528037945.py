N = int(input())
A = list(map(int, input().split()))

A.sort()

edge = [0] * 2
for i in range(2):
    while True:
        l = len(A)
        if len(A) < 2:
            print(0)
            exit(0)

        if A[l-2] == A[l-1]:
            edge[i] = A.pop()
            A.pop()
            break

        A.pop()

print(edge[0] * edge[1])
