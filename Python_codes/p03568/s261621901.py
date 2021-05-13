n = int(input())
a = list(map(int,input().split()))
ans = 1
for i in a:
    if i%2 == 1:
        ans *= 1
    else:
        ans *= 2
print(3**n-ans)