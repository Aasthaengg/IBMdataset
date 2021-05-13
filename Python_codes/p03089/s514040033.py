N = int(input())
B = [int(b) for b in input().split()]

L = []

while B:
    temp = []
    for i in range(len(B)):
        if B[i] == i+1:
            temp.append(i+1)
    if temp:
        L.append(max(temp))
        B.remove(max(temp))
    else:
        break

if B:
    print(-1)
else:
    L.reverse()
    for l in L:
        print(l)