n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)

size = sum(a)
capa = size*2
count = 1

for i,x in enumerate(a[1:]):
    size -= a[i]
    capa = size * 2
    if a[i] <= capa:
        count += 1
    else:
        break

print(count)