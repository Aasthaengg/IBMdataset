n = int(input())

'''
x / y = a ... b -> ay * b = x を今回の問題に当てはめ,N//m = N mod m = kとすると
km + k = N -> N = k(m + 1)となり
k と m + 1 はNの約数となる
また、N mod m < mより
k < mとなり
k < N ** 0.5 
'''
ans = 0
for i in range(1, int(n**.5)+1):
    if n % i or i >= n // i - 1:
        continue
    ans += n // i - 1
print(ans)
