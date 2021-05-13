h,w=map(int,input().split())
m=[]
for i in range(h):
  m.append(list(map(lambda x:int(x=="#"),list(input())))+[0])
m.append([0 for i in range(w+1)])
s=[[100000 for i in range(w+1)] for j in range(h+1)]
s[-1][0]=0
for i in range(h):
  for j in range(w):
    s[i][j]=min(s[i-1][j]+(not(m[i-1][j]) and m[i][j]),s[i][j-1]+(not(m[i][j-1]) and m[i][j]))
print(s[-2][-2])