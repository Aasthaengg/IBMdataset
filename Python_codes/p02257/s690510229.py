n = int(raw_input())
a = []
for i in range(n):
    a.append(int(raw_input()))

nprimes = 0
a = sorted(a)
while True:
    for d in range(2,10001):
        if d**2>a[0]:
            nprimes+=1
            del a[0]
            break
        elif a[0]%d==0:
            del a[0]
            break
    if len(a) <= 0:
        break

print nprimes