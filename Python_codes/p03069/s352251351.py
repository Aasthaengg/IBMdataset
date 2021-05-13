n=int(input())
s=input()

w_num=0
b_num=0
w_l=[0]
b_l=[0]

for i in s:
 if i=='.':
  w_num+=1
 else:
  b_num+=1
 w_l.append(w_num)
 b_l.append(b_num)

ans=10**5
for i in range(n+1):
 ans=min(ans,b_l[i]+(w_num-w_l[i]))
print(ans)