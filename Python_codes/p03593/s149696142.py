H,W = map(int,input().split())
C = {chr(i):0 for i in range(97,123)}
for _ in range(H):
    s = input().strip()
    for j in range(W):
        C[s[j]] += 1
ind1 = 0
for i in range(97,123):
    if C[chr(i)]==1:
        ind1 = C[chr(i)]
D = {0:0, 1:0, 2:0,3:0}
D1 = {0:0,1:0,2:0,3:0}
for c in C:
    D[C[c]%4] += 1
    D1[C[c]%4] += C[c]
if H%2==0 and W%2==0:
    if D[1]==0 and D[2]==0 and D[3]==0:
        flag = "Yes"
    else:
        flag = "No"
elif H%2==0 and W%2==1:
    if D[1]+D[3]>0:
        flag = "No"
    else:
        m = H//2
        if m>=D[2]:
            flag = "Yes"
        else:
            flag = "No"
elif H%2==1 and W%2==0:
    if D[1]+D[3]>0:
        flag = "No"
    else:
        m = W//2
        if m>=D[2]:
            flag = "Yes"
        else:
            flag = "No"
else:
    if D[1]+D[3]!=1:
        flag = "No"
    else:
        m = (H+W-1)//2
        if m>=D[2]:
            flag = "Yes"
        else:
            flag = "No"
print(flag)