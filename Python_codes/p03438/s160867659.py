#APC001_B
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

plus, minus = 0, 0
for i in range(n):
    if a[i] < b[i]:
        plus += (b[i] - a[i]) // 2
    if a[i] > b[i]:
        minus += (a[i] - b[i])
        
print('Yes' if minus <= plus else 'No')