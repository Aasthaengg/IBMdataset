N = int(input())

SP = []
for i in range(1,N+1):
  S,P = input().split()
  SP.append([S,-int(P),i])
  
sort_SP = sorted(SP)

for j in sort_SP:
  print(j[2])