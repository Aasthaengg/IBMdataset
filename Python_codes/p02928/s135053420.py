#第1回日本最強プログラマー学生選手権-予選-B
n,k = map(int,input().split())
a = list(map(int,input().split()))

EPS = 10**9 + 7

cnt = 0
#リストの中身を見る
for i in range(n-1):
    for j in range(i,n):
        if a[i] > a[j]:
            cnt += 1
        
soto = 0
#リスト外
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            soto += 1
            
soto = soto * k * (k-1) // 2

result = cnt * k + soto

print(result % EPS)