n = int(input())
p = list(map(int, input().split()))
ret = 0
for i in range(n-2):
    if p[i] < p[i+1] < p[i+2]:
        ret += 1
    elif p[i+2] < p[i+1] < p[i]:
        ret += 1
print(ret)