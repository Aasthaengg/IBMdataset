H,W,N = map(int,input().split())
d = {}
for _ in range(N):
    a,b = list(map(int,input().split()))
    for dy in range(-1,2):
        for dx in range(-1,2):
            cy = a + dy
            cx = b + dx
            if 2 <= cy <= H-1 and 2 <= cx <= W-1:
                if (cy,cx) not in d:
                    d[(cy,cx)] = 1
                else:
                    d[(cy, cx)] += 1
ans = [0]*10
for v in d.values():
    ans[v] += 1
ans[0] = (H-2)*(W-2) - sum(ans[1:])

for i in range(10):
    print(ans[i])