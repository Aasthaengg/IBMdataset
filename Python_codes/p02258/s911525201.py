a=[]
n=int(input())
i=0
while(n>i):
    b=int(input())
    a.append(b)
    i+=1
score=-1000000000
mini = a[0]
for i in a[1:]:
    if(i-mini>score):
        score = i-mini
    if(mini>i):
        mini=i
    

print(score)