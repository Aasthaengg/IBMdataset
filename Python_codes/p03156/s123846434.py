N=int(input())
A,B=map(int,input().split())
P=input().split()
P_low=[int(x) for x in P if int(x)<=A]
P_normal=[int(x) for x in P if A+1<=int(x)<=B]
P_high=[int(x) for x in P if B+1<=int(x)]


ans=P_low
if len(ans)<=len(P_normal):
    pass
else:
    ans=P_normal
if len(ans)<=len(P_high):
    pass
else:
    ans=P_high
print(len(ans))
