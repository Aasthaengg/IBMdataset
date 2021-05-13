x=int(input())
count=0
t=x//11
k=x-(t*11)
if k==0:
    count+=2*t
elif 1<=k<=6:
    count+=2*t+1
else:
    count+=2*t+2
print(count)