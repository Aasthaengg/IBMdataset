import sys
X = int(input())
L = []
for i in range(1000):
    a = int(i**5)
    L.append(a)
    for j in range(len(L)):
        if X == a-L[j]:
            print(i, j)
            sys.exit()
        elif X == a+L[j]:
            ans = j*-1
            print(i, ans)
            sys.exit()
