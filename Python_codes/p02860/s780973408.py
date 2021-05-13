N=int(input())
S=input()
len_of_s=len(S)
if len_of_s%2==0 and S[:len_of_s//2]==S[len_of_s//2:]:
  print("Yes")
else:
  print("No")