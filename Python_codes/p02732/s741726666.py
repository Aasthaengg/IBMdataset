n = int(input())
a = list(map(int,input().split()))
count = [0]*n
for i in range(n):
    count[a[i]-1] += 1
ans = 0
for i in range(n):
    ans += count[i]*(count[i]-1)//2
for i in a:
    print(ans-count[i-1]+1)