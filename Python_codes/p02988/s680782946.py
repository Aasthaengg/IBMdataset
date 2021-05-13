a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(1,a-1):
    c=sorted([b[i-1],b[i],b[i+1]])
    if c[1]==b[i]:
      count+=1
    else:
        continue
print(count)