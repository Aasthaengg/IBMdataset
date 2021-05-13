e=list(str(input()))
o=list(str(input()))

ln=len(e)+len(o)
ans=['' for i in range(ln)]
for i in range(ln):
    if i %2==0:
        ans[i]=e[i//2]
    else:
        ans[i]=o[(i-1)//2]

print("".join(ans))