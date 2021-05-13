N, M, X = map(int, input().split())
A = list(map(int, input().split()))

A.append(X)
A.sort()

front = []
back = []

while len(A) > 0:
    pop = A.pop(0)
    if pop == X:
        while len(A) > 0:
            back.append(A.pop(0))
    else:
        front.append(pop)

print(min(len(front), len(back)))