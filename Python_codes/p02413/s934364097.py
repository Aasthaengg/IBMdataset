r,_=map(int, input().split())
m=[list(map(int,input().split()))for i in range(r)]
[s.append(sum(s))or print(*s)for s in m]
print(*[sum(c) for c in zip(*m)])