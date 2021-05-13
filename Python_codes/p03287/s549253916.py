import collections
N,M=map(int,input().split())
A=list(map(int,input().split()))
cuml=[0]*(N+1)
l=[]
su=0
for i in range(N):
    su=su+A[i]
    cuml[i+1]=su%M
#print(cuml)
c=collections.Counter(cuml)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
ans=0
#print(values)
for i in range(len(key)):
    ans=ans+(values[i]*(values[i]-1))//2
    #l.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
print(ans)