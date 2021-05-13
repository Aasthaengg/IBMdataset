s=t=0
for i in input():
    if i=="S":s+=1
    elif s>0:s-=1
    else:t+=1
print(s+t)