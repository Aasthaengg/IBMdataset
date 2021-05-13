N, Q=map(int, input().split())
S=input()
count=0
ac=[0]
for i in range(N-1):
  if S[i]=="A" and S[i+1]=="C":
    count+=1
  ac.append(count)
for _ in range(Q):
  l, r=map(int, input().split())
  l-=1
  r-=1
  print(ac[r]-ac[l])