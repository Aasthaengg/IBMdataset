N = int(input())
C = input()

r = C.count('R')
ans = C[:r].count('W')
print(ans)