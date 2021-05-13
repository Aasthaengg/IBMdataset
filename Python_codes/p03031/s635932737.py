N,M=map(int,input().split(' '))
lights=[]
slist=[]

for i in range(M):
  line=input()
  
  switches=list(map(int,line.split(' ')))
  s_bit=0
  for switch in switches[1:]:
    s_bit+=1<<(switch-1)
  slist.append(s_bit)

plist=list(map(int,input().split(' ')))

#print('slist {}'.format(slist))
#print('plist {}'.format(plist))
ans=0
for state_switches in range((1<<N)):
  on_num=0
  #print('====')
  #print(state_switches)
  for k in range(M):
    s_bit=slist[k]
    s_on=s_bit&state_switches
    #print('s_bit state_swithces s_on : {} :{} : {}'.format(s_bit,state_switches,s_on))
    s_num=0
    for i in range(N):
      #print('s_on 1<<i result {} {} {}'.format(s_on,1<<i,s_on&(1<<i))) 
      s_num+=(s_on&(1<<i))>>i
    #print('s_num p {} {}'.format(s_num,plist[k]))
    if s_num%2==plist[k]:
      on_num+=1
    #print(on_num)
  if on_num==M:
    ans+=1

print(ans)
