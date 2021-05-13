s= list(input())
w= int(input())
k=0
t=[]
while k*w<= int(len(s))-1:
  t.append(s[k*w])
  k+=1
  
u=''.join(t)
print(u)