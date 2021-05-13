n = int(input())
ai = list(map(int,input().split()))

even = []

for i in ai:
    if i%2 == 0:
        even.append(i)

ok = 0
for i in even:
    if i%3==0 or i%5==0:
        ok += 1

if len(even) == ok:
    print('APPROVED')
else:
    print('DENIED')
