s=input()

ans=[]

ans.append(s[0])
ans.append(len(s)-2)
ans.append(s[-1])

print(*ans,sep="")