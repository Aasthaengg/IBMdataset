n=int(input())
c=list(map(int, input().split()))
ans = 0
ans2 = 0

for i in c:
    if i%2 == 0:
        ans += 1
        if i%3 ==0 or i%5 == 0:
            ans2 += 1

if ans == ans2:
    print('APPROVED')
if ans != ans2:
    print('DENIED')