import numpy as np

N,K=map(int,input().split())
R,S,P=map(int,input().split())
T1=input()
T2=T1.replace('r', str(P)+' ').replace('s',str(R)+' ').replace('p',str(S)+' ')[:-1]
T2=np.array(list(map(int, T2.split())))

for i in range(N):
  if i >=K and T1[i]==T1[i-K] and T2[i-K] != 0:
    T2[i]=0

print(T2.sum())