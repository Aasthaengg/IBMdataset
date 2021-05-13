a,b,c = map(int,input().split())

sound_count = b//a

if b//a > c:
  print(c)
else:
  print(b//a)