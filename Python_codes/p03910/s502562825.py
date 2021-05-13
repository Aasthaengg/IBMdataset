n=int(input())
i=0
point=0
while n>point:
    i+=1
    point+=i
noneed=point-n
for j in range(1,i+1):
    if j==noneed:
        continue
    print(j)