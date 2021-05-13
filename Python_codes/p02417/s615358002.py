import sys
N=sys.stdin.read()
K=len(N)
N=N.lower()
U=[0]*26
list="abcdefghijklmnopqrstuvwxyz"
for i in range(K):
  for u in range(26):
    if N[i]==list[u]:
      U[u]+=1
for h in range(26):
    print(f"{list[h]} : {U[h]}")
