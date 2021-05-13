s=input()
ls=len(s)
for i in range(2,ls+1,+2):
  ss=s[:ls-i]
  if ss[:len(ss)//2] == ss[len(ss)//2:]:
    print(len(ss))
    exit()
