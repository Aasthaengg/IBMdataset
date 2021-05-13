a,b=input().split()
ST={}
ST[a], ST[b] = map(int, input().split())
ST[input()]-=1

for k,v in ST.items():
  print(v,end=' ')
