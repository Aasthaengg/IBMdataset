n=int(input())
hoge={}
for i in range(n):
  tmp=input()
  if(tmp in  hoge):
    hoge[tmp]+=1
  else:
    hoge[tmp]=1
    
key_max=max(hoge.values())
keys = [k for k, v in hoge.items() if v ==key_max]
hoge=sorted(keys)
for i in range(len(hoge)):
  print(hoge[i])