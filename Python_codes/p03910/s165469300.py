n = int(input())
ng = 0
for i in range(1, n+1):
    if n <= i*(i+1)//2:
        ng = i*(i+1)//2-n
        break

for g in range(1, i+1):
    if g != ng:
        print(g)