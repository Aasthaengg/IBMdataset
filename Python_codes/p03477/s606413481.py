a,b,c,d = map(int,input().split())
ans = a + b -c -d
if ans == 0 :
  print ('Balanced')
if ans >0 :
  print ('Left')
if ans <0:
  print ('Right')