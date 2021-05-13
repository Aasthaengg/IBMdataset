n,l = map(int,input().split())
taste = [0]*n
for i in range(n):
    taste[i] = l+i
api = sum(taste)
eat = 0
sa = 10000
for i in range(n):
    if abs(taste[i]) < abs(sa):
        sa = taste[i]
print(api-sa)