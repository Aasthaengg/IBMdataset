S=str(input())
w=int(input())

SL=len(S)
ans=''

for i in range(0,SL,w):
    ans  += S[i]

print(ans)
