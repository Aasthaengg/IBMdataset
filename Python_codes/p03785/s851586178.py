n,c,k=map(int,input().split())
t=[]
for i in range(n):
  t.append(int(input()))
t.sort()

bus=0
arr=0
que=0
for i in range(n):
  tt=t[i]
  if que==0:
    #print('que=0,i,bus,arr,que,t[i]',i,bus,arr,que,t[i])
    arr=tt
    que+=1
    bus+=1
  else:
    if que==c:
      #print('q==c,i,bus,arr,que,t[i]',i,bus,arr,que,t[i])
      bus+=1
      arr=tt
      que=1
    else:
      if arr+k<tt:
        #print('dep,i,bus,arr,que,t[i]',i,bus,arr,que,t[i])
        bus+=1
        arr=tt
        que=1
      else:
        #print('waiting,i,bus,arr,que,t[i]',i,bus,arr,que,t[i])
        que+=1

print(bus)
