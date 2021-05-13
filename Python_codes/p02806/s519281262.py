n = int(input())
s, t = [], []
for i in range(n):
    a, b = input().split()
    s.append(a)
    t.append(int(b))
x = input()
print(sum(t[s.index(x)+1:]))