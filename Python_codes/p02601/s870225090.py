A, B, C = map(int,input().split())
K = int(input())

flag = False
for i in range(K+1):
    TB = B * (2 ** i)
    TC = C * (2 ** (K-i))
    if TB > A and TC > TB:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
