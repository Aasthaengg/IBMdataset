s=int(input())
target=[s]
i=0

while True:
    if target[i]%2==0:
        tmp=target[i]/2
    else:
        tmp=3*target[i]+1
    if tmp in target:
        i+=1
        break
    else:
        target.append(tmp)
        i+=1
print(i+1)