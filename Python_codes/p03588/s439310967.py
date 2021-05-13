# 2020/02/29
# Tenka1 Programmer Beginner Contest - B

from operator import itemgetter

# Input
n = int(input())
l = list()

for i in range(n):
    ab = list(map(int,input().split()))
    l.append(ab)

l.sort(key=itemgetter(1))

# Calc
ans = l[0][0] + l[0][1]

# Output
print(ans)
