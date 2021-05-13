n = int(input())
a = []
b = []
for i in range(n):
    s,t = map(int,input().split())
    a.append(s)
    b.append(t)
print(max(a)+min(b))