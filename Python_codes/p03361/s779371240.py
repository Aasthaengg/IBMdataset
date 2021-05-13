h,w=map(int,input().split())
S = [["."]*(w+2)]
for i in range(h):
  S.append(["."]+list(input())+["."])
S.append(["."]*(w+2))
for i in range(h+2):
  for j in range(w+2):
    if S[i][j] == "#":
      if S[i+1][j] == "." and S[i-1][j] == "." and S[i][j+1] == "." and S[i][j-1] == ".": 
        print("No")
        quit()
print("Yes")