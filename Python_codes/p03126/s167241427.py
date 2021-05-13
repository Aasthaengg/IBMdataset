n,m = list(map(int, input().split()))

s = set([])
for i in range(1,31):
    s.add(i)

for _ in range(n):
    _,*a = list(map(int, input().split()))
    s &= set(a)

print(len(s))