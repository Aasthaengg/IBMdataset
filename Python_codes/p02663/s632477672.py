from datetime import datetime

H1,M1,H2,M2,K=[int(i) for i in input().split(" ")]

t1=datetime(2020,5,30,H1,M1,0)
t2=datetime(2020,5,30,H2,M2,0)
d=t2-t1
print(d.seconds//60-K)
