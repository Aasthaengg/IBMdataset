n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sum, hoge = 0, 100
for i in range(n):
    sum += b[a[i]-1]
    if hoge + 1 == a[i]:
        sum += c[hoge-1]
    hoge = a[i]
print(sum)