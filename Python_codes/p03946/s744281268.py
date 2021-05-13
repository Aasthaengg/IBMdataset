n,t = map(int,input().split())
a = list(map(int,input().split()))

#リンゴを買う個数
apple = n//2

#街iで売った時の利益
b = []
mi = a[0]
for i in range(n):
    if a[i] < mi:
        mi = a[i]
    b.append((a[i]-mi)*apple)

ma = max(b)

print(b.count(ma))