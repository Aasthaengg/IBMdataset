n = int(input())
xs = [(i, int(v)) for i, v in enumerate(input().split())]

tmp = sorted(xs, key=lambda x: x[1])

a = tmp[n // 2 - 1][1]
b = tmp[n // 2][1]

ans = [0]*n

for i,v in tmp[:n//2]:
    ans[i] = b
    
for i, v in tmp[n//2:]:
    ans[i] = a

for i in ans:
    print(i)
