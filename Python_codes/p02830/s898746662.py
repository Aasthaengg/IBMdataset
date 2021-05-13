N=int(input())
a1=input().split()
S,T=list(a1[0]),list(a1[1])
empty=[]
for i in range(0,N):
    x=S[i]+T[i]
    empty.append(x)
y=''.join(empty)
print(y)