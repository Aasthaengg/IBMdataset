n = int(input())
x = []
s = 0
for i in range(n):
    a,b = map(int,input().split())
    x.append(a+b)
    s += b
x.sort(reverse=True)
print(sum(x[::2])-s)
