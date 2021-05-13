n=int(input())
p=[None]*n
for i in range(n):
    p[i] = int(input())
p.sort(reverse=True)
print(p[0]//2 + sum(p[1:]))