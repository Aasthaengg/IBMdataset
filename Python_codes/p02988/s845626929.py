n = int(input())
l = list(map(int,input().split()))

count = 0
for i in range(n-2):

    if(l[i] < l[i+1] and l[i+1] < l[i+2]):
        count += 1
        continue
    if(l[i+2] < l[i+1] and l[i+1] < l[i]):
        count += 1
        continue

print(count)