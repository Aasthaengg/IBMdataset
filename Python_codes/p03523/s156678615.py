a=["KIH","B","R",""]
ans=[]
aaa=[]
for i in range(16):
    b=""
    for j,k in enumerate(a):
        if ((i >> j) & 1):
            b+="A"
        b+=k
    ans.append(b)
print("YES" if input() in ans else "NO") 