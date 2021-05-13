import datetime
a,b = list(map(int, input().split()))
cnt = 0
pro = datetime.date(2018, a, b)

for i in range(1, 13):
  if(datetime.date(2018, i, i) <= pro):
    cnt +=1
print(cnt)