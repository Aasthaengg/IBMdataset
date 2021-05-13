s = input()
A = int(s[0])
B = int(s[1])
C = int(s[2])
D = int(s[3])

flag = [0]*3
tmp = 0
for i in range(8):
  flag[0]=(i>>2)&1
  flag[1]=(i>>1)&1
  flag[2]=(i)&1
  
  tmp = A +(-1)**flag[0]*B +(-1)**flag[1]*C +(-1)**flag[2]*D
  if tmp==7:
    ans=s[0]
    for j in range(3):
      if flag[j]:
        ans+="-"+s[j+1]
      else:
        ans+="+"+s[j+1]
    ans+="=7"
    print(ans)
    break