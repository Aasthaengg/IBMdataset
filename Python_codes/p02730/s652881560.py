import sys
S=input()
N=len(S)
if S[:N//2]==S[N//2+1:][::-1]:
  if N==3:
    print("Yes")
  elif (N//2)%2==1:
    if S[:(N//2)//2]==S[(N//2)//2+1:N//2][::-1] and S[N//2+1:-(N//2)//2]==S[-(N//2)//2+1:][::-1]:
      print("Yes")
    else:
#      sys.stderr.write("2\n")
      print("No")
  else:
    if S[:(N//2)//2]==S[(N//2)//2:N//2][::-1] and S[N//2+1:-(N//2)//2]==S[-(N//2)//2:][::-1]:
      print("Yes")
    else:
      print("No")
else:
#  sys.stderr.write("1\n")
  print("No")

