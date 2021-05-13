n, m = map(int,input().split())
n += 1
s = input()
Z = []
for i in range(n):
    if s[i] == "0":
        Z.append(i)
D = [-1] * n
i = len(Z)-1

import sys
for j in range(n-1, -1, -1):
    if s[j] == "0":
        while i >= 0 and j - Z[i] <= m:
            i -= 1
        D[j] = Z[i+1]
        # print(D)
        if j != 0 and j <= Z[i+1]:
            print(-1)
            sys.exit()
# print(D)

a = n-1
ANS = []
while a != 0:
    b = D[a]
    ANS.append(a-b)
    a = b

print(" ".join([str(i) for i in ANS[::-1]]))