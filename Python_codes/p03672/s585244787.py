S = input()
s=[]
for i in S:
    s.append(i)
for i in range(len(s)):
  t = s[0:-i-1]
  if t[:len(t)//2]==t[len(t)//2:]:
    print(len(t))
    break