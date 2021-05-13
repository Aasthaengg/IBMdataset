N,X = map(int,input().split())
L = list(map(int,input().split()))
count = 1
posi = 0
for i in L:
    posi +=i
    if(posi<=X):
        count+=1
    else:
        break
print(count)