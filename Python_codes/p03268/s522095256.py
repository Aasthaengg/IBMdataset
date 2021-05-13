N,K = map(int,input().split())
div = []
div2 =[]

for i in range(1,N+1):
    if (i%K == 0):
        div.append(i)
    elif (2*i%K == 0):
        div2.append(i)
    else :
        continue
l1 = len(div)
l2 = len(div2)
print(l2*l2*l2 + l1*l1*l1)