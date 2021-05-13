n = int(input())
s = input()
if len(s)%2 ==1:
  print("No")
  exit()

s_h = s[:int((len(s)/2))]

s_h_2 = s[int((len(s)/2)):]


if s_h == s_h_2:
  print("Yes")
else:
  print("No")