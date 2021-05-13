n=int(input())
dic={}.fromkeys(map(str,input().split()))
if len(dic)==3:
  print("Three")
if len(dic)==4:
  print("Four")