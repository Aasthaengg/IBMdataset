a=int(input())

row=sorted(map(int,input().split()))

cnt=0

for i in range(len(row)):
  for j in range(i+1,len(row)):
    for k in range(j+1,len(row)):
      if row[i]!=row[j] and row[j]!=row[k] and row[i]!=row[k]:
        if (abs(row[j]-row[i]) < row[k]) and (row[k] < row[j]+row[i]):
          cnt+=1

print(cnt)