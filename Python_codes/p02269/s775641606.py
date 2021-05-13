n = int(input())
D = set([])
for i in range(n):
    A,X = input().split()
    if A[0] == "i":
        D.add(X)
    else:
        if X in D:
            print("yes")
        else:
            print("no")
