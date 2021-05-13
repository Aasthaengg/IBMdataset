n = int(input())
s = input()
t = input()
cou = 0
for i in range(n):
  s1 = s[i:]
  t1 = t[:n-i]
#  print(s1,t1)
  if s1==t1:
    print(2*n-(n-i))
    exit()
else:
  print(2*n)
