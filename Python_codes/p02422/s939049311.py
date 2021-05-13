s=input()
for _ in range(int(input())):
 a=input().split()
 if a[0]=='print':print(s[int(a[1]):int(a[2])+1])
 else:
  t=s[0:int(a[1])]
  t+=s[int(a[1]):int(a[2])+1][::-1]if'reverse'==a[0]else a[3]
  s=t+s[int(a[2])+1:]