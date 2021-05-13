from itertools import accumulate

n = int(input())
As = list(map(int, input().split()))
As.sort()
acc = [0] + list(accumulate(As))
# print(As, acc)
"""
それまでの累積和が次のやつを食うかどうか
食えない⇨それ以前はいくら頑張ってもダメ
1 2 7 20 30 40
1 3 10 30 60 100 
"""
for i in range(1,n+1):
    if i == 0:continue
    if As[-i] > acc[-i-1]*2:
        break
print(i)
