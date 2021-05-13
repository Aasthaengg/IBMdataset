import itertools

n = int(input())

l = list(itertools.product([0,1], repeat=n))[::-1]

A = {}
for i in range(n):
    ai = int(input())
    for j in range(ai):
        x, y = map(int, input().split())
        if i not in A:
            A[i] = []
        A[i].append((x, y))
    if ai == 0:
        A[i] = []


def shoujiki(i):
    check = {}
    cnt = 0
    for j in range(n):
        check[j+1] = i[j]
    for j in range(n):
        ai = len(A[j])
        if i[j] == 1:
            for k in range(ai):
                x, y = A[j][k]
                if check[x] != y:
                    return 0
    #return (check, shougen, cnt0, cnt)
    return sum(i)

mans = 0
for i in l:
    mans = max(shoujiki(i), mans)

print(mans)
