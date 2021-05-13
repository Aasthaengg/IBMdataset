s = input()

s1 = int(s[0])*10 + int(s[1])
s2 = int(s[2])*10 + int(s[3])
#print(s1, s2)
if  (s1>12 or s1==0) and (s2>12 or s2==0):
  print('NA')
elif (s1>12 or s1==0) and 1<=s2<=12:
  print('YYMM')
elif (s2>12 or s2==0) and 1<=s1<=12:
  print('MMYY')
elif 1<=s1<=12 and 1<=s2<=12:
  print('AMBIGUOUS')