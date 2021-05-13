import sys

S=input()
N=len(S)
if S!=S[::-1]:
  print("No")
  sys.exit(0)
check=S[0:int((N-1)/2)]
#print(check)
if check!=check[::-1]:
  print("No")
  sys.exit(0)
check=S[int((N+3)/2)-1:N]
#print(check)
if check!=check[::-1]:
  print("No")
  sys.exit(0)
print("Yes")