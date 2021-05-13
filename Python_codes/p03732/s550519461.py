n,max_w = map(int,input().split())
w1=[]
w2=[]
w3=[]
w4=[]
v1=[]
v2=[]
v3=[]
v4=[]

w_1,v_1 = map(int,input().split())
w1.append(w_1)
v1.append(v_1)

for i in range(1,n):
  tmp_w,tmp_v = map(int,input().split())
  if tmp_w == w_1:
    w1.append(tmp_w)
    v1.append(tmp_v)
  elif tmp_w == w_1+1:
    w2.append(tmp_w)
    v2.append(tmp_v)
  elif tmp_w == w_1+2:
    w3.append(tmp_w)
    v3.append(tmp_v)
  elif tmp_w == w_1+3:
    w4.append(tmp_w)
    v4.append(tmp_v)
  

count1 = len(w1)
count2 = len(w2)
count3 = len(w3)
count4 = len(w4)

v1 = sorted(v1,reverse=True)
v2 = sorted(v2,reverse=True)
v3 = sorted(v3,reverse=True)
v4 = sorted(v4,reverse=True)

ruiseki_v1 = [0]*count1
ruiseki_v2 = [0]*count2
ruiseki_v3 = [0]*count3
ruiseki_v4 = [0]*count4

if v1:
  ruiseki_v1[0]=v1[0]
  for i in range(count1-1):
    ruiseki_v1[i+1]=ruiseki_v1[i]+v1[i+1]

if v2:
  ruiseki_v2[0]=v2[0]
  for i in range(count2-1):
    ruiseki_v2[i+1]=ruiseki_v2[i]+v2[i+1]

if v3:
  ruiseki_v3[0]=v3[0]
  for i in range(count3-1):
    ruiseki_v3[i+1]=ruiseki_v3[i]+v3[i+1]

if v4:
  ruiseki_v4[0]=v4[0]
  for i in range(count4-1):
    ruiseki_v4[i+1]=ruiseki_v4[i]+v4[i+1]

ruiseki_v1.insert(0,0)
ruiseki_v2.insert(0,0)
ruiseki_v3.insert(0,0)
ruiseki_v4.insert(0,0)

ans = 0 
for i in range(count1+1):
  for j in range(count2+1):
    for k in range(count3+1):
      for l in range(count4+1):
        if i*w_1 + j*(w_1+1) + k*(w_1+2) +l*(w_1+3) <= max_w:
          ans = max(ans,ruiseki_v1[i]+ruiseki_v2[j]+ruiseki_v3[k]+ruiseki_v4[l])
print(ans)