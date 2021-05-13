no="UNRESTORABLE"

s=input()
t=input()
ans=list(s[:])
hatena=[ s[i]=="?" for i in range(len(s))]

left=0 ; right=len(s)
while right>=len(t):
    for i in range(right-len(t), right):
        if s[i]!="?" and s[i]!=t[i-right+len(t)]:
            break
    else:
        # hatena[right-len(t):right]=[i*2 for i in hatena[right-len(t):right]]
        ans[right-len(t):right]=list(t) 
        print( ("".join(ans)).replace("?","a") )
        exit()
    right-=1



# for i in range(len(hatena)):
#     if i==0:
#         s+=s[i]
#     elif i==1:
#         s+="a"
print(no)

