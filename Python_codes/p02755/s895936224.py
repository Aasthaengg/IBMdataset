A,B=map(int,input().split())
for i in range(1,1010):
  if (i*100*0.08)//100==A and (i*100*0.1)//100==B:
    print(i)
    break
else:
  print(-1)