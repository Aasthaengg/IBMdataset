N=int(input())
S = list(input())
num=len(S)
if num<=N:
    print(*S,sep='')
else:
    for i in range(N):
          print(S[i], end='')
    print("...")