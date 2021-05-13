n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)-1,-1,-1):
    if a[i]%2==0:
        while(a[i]%2==0):
            cnt+=1
            a[i]/=2
print(cnt)