s=input()
for i in range(1,len(s)//2):
  t=s[:-2*i]
  half=len(t)//2
  if t[:half]==t[half:]:
    print(len(t))
    break