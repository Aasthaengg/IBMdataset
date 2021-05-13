N = int(input())
S, T = (str(x) for x in input().split())
ANS = []
for i in range(N):
  ANS.append(S[i])
  ANS.append(T[i])
  
print(*ANS, sep='')