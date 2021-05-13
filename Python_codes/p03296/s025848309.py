N = int(input())
a = list(map(int,input().split()))
tmp = max(a)+1
count = 0
for i in range(1,N):
    if a[i-1]==a[i]:
        a[i] = tmp
        count+=1
print(count)
