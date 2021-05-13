H,W=map(int,input().split())
L=[[0 for i in range(W)] for j in range(H)]
for i in range(H):
  L1=list(input())
  L[i]=L1
L = [["."] + i + ["."] for i in L]
L = [["." for i in range(W+2)]] + L + [["." for i in range(W+2)]]
for i in range(H+2):
  for j in range(W+2):
    if L[i][j]=="#":
      if L[i][j+1]==L[i][j-1]==L[i+1][j]==L[i-1][j]==".":
        print("No")
        exit()
print("Yes")