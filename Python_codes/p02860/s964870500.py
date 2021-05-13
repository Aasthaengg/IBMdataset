import sys

n = int(input())
s = input()

compare_check = 0
if (len(s) <= 1) or ((len(s)%2) == 1) :
  print("No")
  sys.exit()
else:
  for i in range(len(s)//2):
    if (s[i] == s[i+len(s)//2]):
      compare_check += 1

if ((len(s)//2) == compare_check) :
  print("Yes")
else:
  print("No")