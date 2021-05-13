n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = 0
    ai = a[i]
    while(ai%2==0):
        ai = ai//2
        x+=1
    ans+=x
print(ans)
