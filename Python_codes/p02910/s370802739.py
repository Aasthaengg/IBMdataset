import sys

S = input()

def check():
  for i in range(len(S)) :
    if i%2!=0 and S[i]=="R" :
      print("No")
      sys.exit(0)
    elif i%2==0 and S[i]=="L" :
      print("No")
      sys.exit(0)
check()
print("Yes")
sys.exit(0)