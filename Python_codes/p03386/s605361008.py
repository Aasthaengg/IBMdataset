A,B,K=map(int,input().split())
l=[]
for i in range(A,min(A+K,B+1)):l.append(i)
for i in range(max(B-K+1,A),B+1):l.append(i)
l=sorted(list(set(l)))
for i in l:print(i)