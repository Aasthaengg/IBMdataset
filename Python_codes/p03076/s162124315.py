li=[]
for i in range(5):
    li.append(int(input()))

min=9

min_f=0

for i in range(5):
    if min> li[i]%10 >0:
        min=li[i]%10
        min_f=i

cnt=0

for i in range(5):
    if i==min_f:
        continue
    if li[i]%10==0:
        cnt+=li[i]
    else:
        cnt+=li[i]+10-li[i]%10
print(cnt+li[min_f])