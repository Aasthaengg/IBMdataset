H,W = map(int,input().split())
S = ["."*(W+2)]+["."+input()+"." for h in range(H)]+["."*(W+2)]

for h in range(1,H+1):
  for w in range(1,W+1):
    if S[h][w]=="#" and S[h-1][w]=="." and S[h+1][w]=="." and S[h][w-1]=="." and S[h][w+1]==".":
      print("No")
      exit()
      
print("Yes")
