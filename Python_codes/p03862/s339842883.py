#6問目
N, x = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(N-1):
    #まず一番前の要素がxより小さくなければならない
    if(i == 0 and a[i] > x):
        count += a[i] - x
        a[i] = x
        
    if(a[i] + a[i+1] > x):
        count += a[i] + a[i+1] - x
        a[i+1] = x - a[i]
print(count)