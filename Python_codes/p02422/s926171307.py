s=input()
for _ in range(int(input())):
 a=input().split()
 i=int(a[1]);j=int(a[2])
 if a[0][0]=='p':print(s[i:j+1])
 else:
  t=a[3]if'p'==a[0][2]else s[i:j+1][::-1]
  s=s[0:i]+t+s[j+1:]