S=input()
W=int(input())
for i in range((len(S)+W-1)//W):
  print(S[i*W],end="")