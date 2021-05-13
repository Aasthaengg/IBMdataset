# 2020/04/30
# AtCoder Grand Contest 004 - A

# Input
abc = list(map(int,input().split()))

# Even Check
evenflg = False
for i in range(3):
    if abc[i] % 2 == 0:
        evenflg = True
        break

if evenflg:
    ans = 0
else:
    abc.sort()
    ans = abc[0] * abc[1]

# Output
print(ans)
