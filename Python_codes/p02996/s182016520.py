import bisect

N = int(input())

L = []
for i in range(N):
    a,b = map(int, input().split())
    L.append([b,a])
L.sort()

Sum = 0

for i in range(N):
    Sum = Sum + L[i][1]
    if Sum <= L[i][0]:
        continue
    else:
        print("No")
        quit()
print("Yes")