n = int(input())
a = list(map(int,input().split()))
p = sum(a) / n
t = []
for i in a:
    t.append(abs(p-i))
p = min(t)
print(t.index(p))