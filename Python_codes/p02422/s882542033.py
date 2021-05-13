s=input()
for _ in range(int(input())):
 a=input().split()
 if a[0]=='print':print(s[int(a[1]):int(a[2])+1])
 if a[0]=='reverse':
  s=s[0:int(a[1])]+s[int(a[1]):int(a[2])+1][::-1]+s[int(a[2])+1:]
 if a[0]=='replace':
  s=s[0:int(a[1])]+a[3]+s[int(a[2])+1:]