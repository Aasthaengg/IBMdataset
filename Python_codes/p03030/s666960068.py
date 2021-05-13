N=int(input())
S=[""]*N
T=[""]*N
for i in range(N):
  S[i]=list(input().split())
  S[i][1]=-int(S[i][1])
  T[i]=S[i]
S.sort(key=lambda x:(x[0],x[1]))
for i in range(N):
  for j in range(N):
      if(T[j]==S[i]):
        print(j+1)