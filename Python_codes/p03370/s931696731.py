n,x = map(int,input().split())
mi = [0]*n
for i in range(n):
    mi[i] = int(input())
summi = sum(mi)
nokori = x - summi
count = nokori // min(mi)
count += n
print(count)