n,k = map(int,input().split())
hl = list(map(int,input().split()))
count = 0

for i in hl:
    if i >= k:
        count+=1
print(count)