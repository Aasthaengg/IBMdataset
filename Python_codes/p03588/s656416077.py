n = int(input())
a = []
b = []
for hoge in range(n):
         aa,bb = map(int,input().split())
         a.append(aa)
         b.append(bb)
print((max(a))+(b[a.index(max(a))]))
