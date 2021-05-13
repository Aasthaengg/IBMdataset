#A
stri=input()
ans=0
s=0
for i in range(3):
    if stri[i]=="R":
        s+=1
    else:
        if ans<s:
            ans=s
        s=0
if ans<s:
    ans=s
print(ans)