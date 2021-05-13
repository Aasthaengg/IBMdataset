import datetime
h1,m1,h2,m2,k = map(int,input().split())
end = datetime.datetime(2020,6,6,h2,m2)
start = datetime.datetime(2020,6,6,h1,m1)
#print(start,end)
sub = end-start-datetime.timedelta(minutes=k)
print(sub.seconds//60)