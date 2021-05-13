from collections import Counter
N=int(input())
b=0
S=[]

for i in range(0,N):
    S.append(input())
b=Counter(S)
print(len(b))
