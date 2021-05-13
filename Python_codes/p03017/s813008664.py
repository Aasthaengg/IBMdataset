N,A,B,C,D = map(int,input().split())
S = input()

if "##" in S[A-1:max(C,D)-1]:
  print("No")
  exit()
if C < D:
  print("Yes")
  exit()

count = 0
for i in range(B-1,D):
  if D != len(S): 
    if S[i] == "." and S[i-1] == "." and S[i+1] == ".":
      print("Yes")
      exit()
print("No")