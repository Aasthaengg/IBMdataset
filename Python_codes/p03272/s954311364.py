n,i=map(int,input().split())

train=[]
js=0

for x in range(1,n+1):
    train.append(x)
    
train=train[::-1]

for x in train:
    js +=1
    if x==i:
        print(js)
        break