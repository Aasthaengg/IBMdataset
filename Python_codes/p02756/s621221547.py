S = input().strip()
L = []
R = []
Q = int(input())
flag = 0
for _ in range(Q):
    q = list(input().split())
    if len(q)==1:
        flag = 1-flag
    else:
        F = q[1]
        C = q[2]
        if flag==0 and F=="1":
            L.append(C)
        elif flag==0 and F=="2":
            R.append(C)
        elif flag==1 and F=="1":
            R.append(C)
        elif flag==1 and F=="2":
            L.append(C)
L = "".join(L)
R = "".join(R)
if flag==1:
    S = S[::-1]
    R = R[::-1]
    S = R+S+L
else:
    L = L[::-1]
    S = L+S+R
print(S)