""" スニペット """
def get_int():
	return int(input())

def get_ints():
	return list(map(int, input().split()))
""" スニペット """
import math
# 2つ選ぶ通り数を算出 nC2
def choose2(n):
    return math.floor(n*(n-1)/2)

# インプット
N = get_int()
An = get_ints()
""" 全ての要素から2つのボールを選ぶ通り数を求める """
uni = [0] * (N+1)
# ユニーク数の配列を求める
for i in range(N):
    uni[An[i]] += 1
sumWay = 0
# 各数値の2通りの選択通り数を足していく ここのindex=0がいらない
for i in range(N+1):
    sumWay += choose2(uni[i])
""" 全ての要素数 - 削除する要素の通り数 + 削除する要素を引いた際の通り数 を求める """
for i in range(N):
    print(sumWay - choose2(uni[An[i]]) + choose2(uni[An[i]]-1)) 