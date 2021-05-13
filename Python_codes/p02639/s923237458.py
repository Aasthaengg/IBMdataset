a,b,c,d,e = map(int,input().split())

x = [a,b,c,d,e]

for i in range(len(x)):
  if x[i] == 0:
    print(i+1)