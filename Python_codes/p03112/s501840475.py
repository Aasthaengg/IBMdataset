A, B, Q = map(int, input().split())

S = [0]*A
for i in range(A):
  S[i] = int(input())

T = [0]*B
for i in range(B):
  T[i] = int(input())

import bisect
ans = []
for i in range(Q):
  mini = 10**11
  x = int(input())
  indS = bisect.bisect(S,x)
  indT = bisect.bisect(T,x)
  if indS != A: #Sの右
    if indT != B:
        mini = min(max(S[indS],T[indT])-x,mini) #右右
        # print('rr',mini)
    if indT != 0:
        mini = min(S[indS]-T[indT-1]+min(S[indS]-x,x-T[indT-1]),mini) #右左
        # print('rl',mini)
  if indS != 0: #Sの左
    if indT != B:
        mini = min(T[indT]-S[indS-1]+min(x-S[indS-1],T[indT]-x),mini)  #左右
        # print('lr',mini)
    if indT != 0:
        mini = min(x-min(S[indS-1],T[indT-1]),mini) #左左
        # print('ll',mini)
  ans.append(mini)



# print(ans)
print(*ans, sep='\n')