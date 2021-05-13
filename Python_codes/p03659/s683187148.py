N = int(input())
a = list(map(int,input().split()))
sunuke,arai = a[0],sum(a)-a[0]
A = [abs(sunuke-arai)]
for i in range(1,N-1):
    sunuke += a[i]
    arai -= a[i]
    A.append(abs(sunuke - arai))
print(min(A))