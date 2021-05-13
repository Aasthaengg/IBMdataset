r,l = map(int,input().split())
if l-r+1 >= 2019:
    print("0")
    exit()
li = []
for i in range(l-r+1):
    li.append((r+i)%2019)
li.sort()
lia = []
for i in range(len(li)):
    for j in range(len(li)):
        if i != j:
            lia.append((li[i]*li[j])%2019)
print(min(lia))