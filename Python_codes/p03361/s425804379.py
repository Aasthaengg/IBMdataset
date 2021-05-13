h,w = map(int, input().split())
S = [list(input()) for i in range(h)]
for i in range(h):
  S[i] = ["."] + S[i] + ["."]
S.insert(0, ["."]*(w+2))
S.append(["."]*(w+2))

for i in range(1,h+1):
  for j in range(1,w+1):
    if S[i][j] == ".":
      pass
    else:
      if [S[i-1][j],S[i+1][j],S[i][j-1],S[i][j+1]] == ["."]*4:
        print("No")
#        print(i,j)
        exit()
      
print("Yes")