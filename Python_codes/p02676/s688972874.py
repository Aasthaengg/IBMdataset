N=int(input())
S=list(input())
if len(S)<=N:
   for i in range(len(S)):
       print(S[i],end="")
else:
    for i in range(N):
        print(S[i],end="")
    print("...")