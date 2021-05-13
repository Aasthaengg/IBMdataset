n = int(input())
l = list(map(int,input().split()))
ans = 0
mini = 10**8
for i in range(n):
    num = 0
    while l[i] %2==0:
        num += 1
        l[i] /= 2
    mini = min(mini,num)
print(mini)
