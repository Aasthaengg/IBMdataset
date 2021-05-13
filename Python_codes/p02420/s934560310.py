mozi=[input()]
ans=[]
i=0


while mozi[i] != '-':
    num=0
    
    for w in range(int(input())):
        num=num + int(input())
        
    for w in range(num):
        mozi[i] = mozi[i][1:] + mozi[i][0:1]
        
    mozi.append(input())
    i=i+1

i=0
while mozi[i] != '-':
    print(mozi[i])
    i=i+1
