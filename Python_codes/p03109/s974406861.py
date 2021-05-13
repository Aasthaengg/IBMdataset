s = list(input().split('/'))
s = [int(ss) for ss in s]

if s[0] < 2019:
  print("Heisei")
elif s[0] == 2019:
  if s[1] < 4 or (s[1] == 4 and s[2] <= 30):
    print("Heisei")
  else:
    print("TBD")
else:
  print("TBD")
