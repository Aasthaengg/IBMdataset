
import bisect
X = int(input())
n = 10**5+3
sosu = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    sosu.difference_update(range(i*2, n+1, i))
sosu = list(sosu)
sosu.sort()
ind = bisect.bisect_right(sosu, X)
if sosu[ind-1] == X:
    print(X)
else:
    print(sosu[ind])
