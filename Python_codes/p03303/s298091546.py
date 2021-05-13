S=input()
w=int(input())
ans=[]
for i in range(0,len(S),w):
  ans.append(S[i])
print("".join(ans))
