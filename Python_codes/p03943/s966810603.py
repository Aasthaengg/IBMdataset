L = [int(x) for x in input().split()]
L.sort()
if L[0] + L[1] == L[2]:
    print("Yes")
else:
    print("No")