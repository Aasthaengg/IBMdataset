N = int(input())
A = list(map(int, input().split()))

count = 0
min = abs(A[0])
sum = 0
for i in A:
    # 0と負の数をカウント
    if i<=0:
        count += 1
    # 最小更新
    if min > abs(i):
        min = abs(i)
    # 合計
    sum += abs(i)
#print('count:'+str(count))
#print('min:'+str(min))
#print('sum:'+str(sum))
if count%2 == 0:
    print(sum)
else:
    print(sum-(min*2))
