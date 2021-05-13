
S = input()
List=[0]*(len(S)+1)
i=0
while i<len(S):
    if S[i]=="<":
        List[i+1]=List[i]+1
    i+=1
j=1
while j<=len(S):
    if S[-j]==">":
        List[-(j+1)]=max(List[-j]+1,List[-(j+1)])
    j+=1
print(sum(List))