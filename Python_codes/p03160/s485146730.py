n = int(input())
li = list(map(int,input().split()))

dp = [0,abs(li[1]-li[0])]

for i in range(2,n):
    dp += [min(dp[-2]+abs(li[i]-li[i-2]),dp[-1]+abs(li[i]-li[i-1]))]

print(dp[-1])