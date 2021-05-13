N=int(input())
L=list(map(int,input().split(' ')))

N_tri=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if L[i] != L[j] and L[j]!=L[k] and L[k]!=L[i]:
        L_sorted=sorted([L[i],L[j],L[k]])
        if L_sorted[0]+L_sorted[1]>L_sorted[2]:
          N_tri+=1

print(N_tri)