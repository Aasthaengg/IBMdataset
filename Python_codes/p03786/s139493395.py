N = int(input())
a = list(map(int,input().split()))
a.sort()

for i in range(1,N):
    a[i] = a[i-1] + a[i]
cnt = 1
for i in reversed(range(1,N)):
    if(a[i] > a[i-1] * 3): 
        break
    cnt += 1
print(cnt)
