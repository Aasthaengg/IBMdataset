input()
S = input()

ans = 0
tmp = 0

for si in S:
    tmp += [-1,1][si=='I']
    ans = max(ans,tmp)

print(ans)