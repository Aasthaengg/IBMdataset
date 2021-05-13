n = int(input())
p = [int(input()) for i in range(n)]

maxkun = max(p)//2
p.remove(max(p))
print(maxkun + sum(p))