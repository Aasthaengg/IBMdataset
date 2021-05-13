N = int(input())
L = list(map(int,input().split()))
L.sort()
a = L[-1]
b = sum(L[:-1])
if a < b:
    print("Yes")
else:
    print("No")