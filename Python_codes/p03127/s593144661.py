n = int(input())
A = list(set(list(map(int, input().split()))))
A.sort()

while not len(A) == 1:
    div = A[0]
    A = A[1:]
    A = list(map(lambda x:x%div, A))
    A.append(div)
    A = list(set([x for x in A if x != 0]))
    A.sort()

print(A[0])