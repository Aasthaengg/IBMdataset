N = int(input())
a, b = [], []
for i in range(N):
    a0, b0 = map(int, input().split())
    a.append(a0)
    b.append(b0)
a, b = zip(*sorted(zip(a, b)))
ans = a[-1]+b[-1]
print(ans)

    
