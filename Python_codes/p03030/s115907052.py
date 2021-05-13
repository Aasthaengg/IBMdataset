N=int(input())
L=[list(input().split())+[i+1] for i in range(N)]
L=[[l[0],int(l[1]),l[2]] for l in L]
L.sort(key=lambda x: x[1],reverse=True)
L.sort(key=lambda x: x[0])
for l in L:
  print(l[2])