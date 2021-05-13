import collections
H,W = list(map(int , input().split()))
D = []
for j in range(H):
    x=list(input())
    D.extend(x)
s = len(list((set(D))))
c = collections.Counter(D)
Q = []

for i in range(s):
    Q.append(c.most_common()[i][1])
if s == 1:
    print("Yes")
else:
    if ((H*W)%2 == 1):
        seigen = (H//2+1)*(W//2 +1)
        q = 0
        m = 0
        mm = (H*W-(H//2)*(W//2)*4)//2+1
        for k in range(s):
            q += (Q[k] % 2)
            if (Q[k] % 4)!= 0:
                m += 1
        if (q == 1)and(s<=seigen)and (m <= mm):
            print("Yes")
        else:
            print("No")
    elif ((H%2) == 0)and((W %2) ==0):
        seigen = (H*W)//4
        q = 0
        for k in range(s):
            q += (Q[k] % 4)
        if ((s <= seigen)and(q == 0)):
            print("Yes")
        else:
            print("No")

    else:
        q = 0
        e = 0
        if ((H%2) == 1):
            seigen = (H//2+1)*W
            seigen2 = W//2
        elif ((W%2) == 1):
            seigen = (W//2+1)*H
            seigen2 = H//2
        for k in range(s):
            q += (Q[k] % 2)
            if (Q[k] % 4)!= 0:
                e += 1
        if (q == 0)and(s<=seigen)and(e<=seigen2):
            print("Yes")
        else:
            print("No")
