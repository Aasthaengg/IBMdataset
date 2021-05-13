N=int(input())
l=[]
for i in range(N):
    S,P=map(str,input().split())
    b=' '
    if len(S)<10:
        S=S+b*(10-len(S))
    P=(100-int(P))
    l.append([S+str(P).zfill(3),i])
l.sort()

for i in range (N):
    print(l[i][1]+1)