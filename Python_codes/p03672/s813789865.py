s=input()
s=s[:-1]
while True:
  if len(s)%2==0 and s[len(s)//2:]==s[:len(s)//2]:
    print(len(s))
    break
  else:
    s=s[:-1]
    continue