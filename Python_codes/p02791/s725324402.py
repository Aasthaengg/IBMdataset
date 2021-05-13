n = int(input())
l = list(map(int,input().split()))
m = l[0]
count = 1
for i in range(1,n):
    if m > l[i]:
        count += 1
        m = l[i]
print(count)