N, K = map(int, input().split())
pList = list(map(int, input().split()))
#範囲内の和を求めるには累積和とういうのを使う
#事前準備
cum_sum_list = [0]*(N+1)
cum_sum = 0
pListLen = len(pList)
for i in range(pListLen):
  cum_sum += pList[i]
  cum_sum_list[i+1] = cum_sum
#範囲内の和を比べていく
max_sumK = 0
max_start = 0
max_end = 0
for i in range(N-K+1):
  start = i
  end = (i+K)
  sumK = cum_sum_list[end] - cum_sum_list[start]
  if (sumK > max_sumK):
    max_sumK = sumK
    max_start = start
    max_end = end
#最大の期待値を計算して出力
answer = 0
for num in pList[max_start:max_end]:
  answer += sum(list(range(1, (num+1))))/num
print(answer)
