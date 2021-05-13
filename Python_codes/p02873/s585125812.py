# <>>><<><<<<<>>><
# >< is 0
S = input()
part = S.replace('><','> <').split(' ')

ans=0
for p in part:
    left  = p.count('<')
    right = p.count('>')
    ans += sum(range(1, max(left, right) + 1))
    ans += sum(range(1, min(left, right)))

print(ans)

