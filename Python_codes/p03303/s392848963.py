S=input()
w=int(input())

ans=[]
cnt=0
while(w*cnt+1<=len(S)):
    ans.append(S[w*cnt])
    cnt+=1

print("".join(map(str,ans)))