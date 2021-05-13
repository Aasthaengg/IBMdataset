N=int(input())

statements=[]
honests=[0]
for i in range(N):
  statement=[]
  A=int(input())
  for j in range(A):
    x,y=map(int,input().split(' '))
    statement.append([x-1,y]) 
  statements.append(statement)

#print(statements)
ans=0

for honest in range(1<<N):
  flag=True
  for j in range(N):
    statement=statements[j]
    for x,y in statement:
      if (honest&(1<<j))>>j ==1:
        flag*=((honest&(1<<x))>>x ==y)


    #print(flag)
  if flag==True:
    honests.append(honest)

n_honests=[]
for honest in honests:
  n_honest=0
  for i in range(N):
    n_honest+=(honest&(1<<i))>>i
  n_honests.append(n_honest)

print(max(n_honests))
