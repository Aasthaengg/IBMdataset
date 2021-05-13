# ACB054A
import sys
n, m = map(int, input().split())
N = []
M = []
for i in range(n):
    N.append(input())
for i in range(m):
    M.append(input())

for i in range(n-m+1):
    if M[0] not in N[i]:
        continue
    else:
        ind = N[i].index(M[0])
        A = True
        for j in range(m):
            if M[j] != N[i+j][ind:ind+m]:
                A = False
                break
        if A:
            print("Yes")
            sys.exit()
print("No")
