N = list(map(int,input().split()))
S = list(input())


for i in range(len(S)):
  if i+1 == N[1]:
    print(str.lower(S[N[1]-1]),end="")
  else:
  	print(S[i],end="")
