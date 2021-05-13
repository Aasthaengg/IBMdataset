N = int(input())
a = list(map(int, input().split()))
suma = sum(a)
sunuke = a[0]
arai = suma-a[0]
mi = abs(sunuke-arai)
for i in range(1,N-1):
    sunuke += a[i]
    arai -= a[i]
    mi = min(mi,abs(sunuke-arai))
print(mi)