import math

N = int(input())
leaf = list(map(int,input().split()))

end_flag = False
count = sum(leaf)
ans = 0
node = 1

for i in range(N+1):
    if end_flag:
        break
    ans += node
    count -= leaf[i]
    node = min(count, (node-leaf[i])*2)

    if node < 0:
        end_flag = True

if end_flag:
    print('-1')
else:
    print(ans)