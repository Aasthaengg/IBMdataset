a = "keyence"
S = input().strip()
N = len(S)
flag = 0
for i in range(N):
    if flag==0 and i<len(a) and S[i]==a[i]:continue
    elif flag==0 and i<len(a) and S[i]!=a[i]:
        flag = 1
        cur = i
        break
if flag==0:
    print("YES")
else:
    if S[-(7-cur):]==a[cur:]:
        print("YES")
    else:
        print("NO")