import math
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

pls = 0
for i in reversed(range(N)):
    a, b = AB[i]
    temp = (math.ceil((a + pls) / b))
    pls += b*temp - (a + pls)
print(pls)