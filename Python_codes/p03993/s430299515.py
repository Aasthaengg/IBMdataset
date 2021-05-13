n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    if(a[a[i]-1] == i+1):
        count += 1
print(int(count/2))