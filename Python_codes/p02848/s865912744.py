n=int(input())
s=input()

l=[]

for a in s:
  moji=ord(a)
  moji+=n

  if int(moji)>90:
    moji-=26

  l.append(chr(moji))

print(''.join(l))