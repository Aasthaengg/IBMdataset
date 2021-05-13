N, K = list(map(int, input().split()))
num = 0
#奇数の数を求める
for n in range(1,N+1):
    if n%2!=0:
        num += 1
if num<K:
    print("NO")
else:
    print("YES")