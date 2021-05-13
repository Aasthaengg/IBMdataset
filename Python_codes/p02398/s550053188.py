line = list(map(int,input().split()))
count = 0
for i in range(line[0],line[1]+1):
    if line[2]%i==0: count+=1
print(count)