N = int(input())
ls = list(map(int,input().split()))
keta = []
ans = 'a'
j = 0
while ans == 'a':
    for i in range(N):
        if ls[i]%2 == 0:
            ls[i] = ls[i]//2
        else:
            ans = j
            break
    j += 1
print(ans)