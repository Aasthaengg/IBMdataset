data =input()
data = list(data)
deter =""
cnt2 =0
cnt =[0]*5
cnt3 =0
for t in range(len(data)):
  if data[t] =="I":
    cnt[0] +=1
  if data[t] =="K":
    cnt[1] +=1
  if data[t] =="H":
    cnt[2] +=1
  if data[t] =="B":
    cnt[3] +=1
  if data[t] =="R":
    cnt[4] +=1
  
if cnt[0] ==1 and cnt[1] ==1 and cnt[2] ==1 and cnt[3] ==1 and cnt[4] ==1:
  cnt2 +=1 

if len(data) >9 or cnt2 ==0 :
  print("NO")
  cnt3 +=1
if len(data) >=5 and len(data)<=9  and cnt2 ==1:
  if data[0] !="A":
    data.insert(0,"A")
  if data[4] !="A":
    data.insert(4,"A")
  if data[6] !="A":
    data.insert(6,"A")
  if len(data) ==8:
    data.append("A")
  else:
    if data[8] !="A":
      data.insert(8,"A")
 
  for s in range(len(data)):
    deter +=data[s]
  
  if deter =="AKIHABARA":
    print("YES")
  else:
    print("NO")

 
if len(data) <=4 and cnt3==0:
  print("NO")
