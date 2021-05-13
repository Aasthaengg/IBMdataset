n = int(input())
l = list(map(int,input().split()))

ans = 0
for i in range(n):
    ans = (ans ^ l[i])

for i in range(n):
    print(ans ^ l[i])