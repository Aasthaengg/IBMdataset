n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
li = [0]*(n+1)
for i in p:
    li[i] = li[i-1]+1
print(n-max(li))