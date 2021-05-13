n = int(input())
ma = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    ma.append(tmp)
ma.reverse()

count = 0
for m in ma:
    a = m[0]+count
    b = m[1]
    if a == 0:
        #count += b
        continue
    if a%b != 0:
        amari = a%b
        addition = b - amari
        count += addition
print(count)