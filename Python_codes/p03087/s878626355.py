N,Q=map(int,input().split())
S=input()
tot=[0]
for i in range(N-1):
    if S[i:i+2]=="AC":
        tot.append(tot[-1]+1)
    else:
        tot.append(tot[-1])

for q in range(Q):
    l,r=map(int,input().split())
    print(tot[r-1]-tot[l-1])