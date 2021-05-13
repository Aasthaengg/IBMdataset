def round_up_division(num1, num2):
# 切り上げ除算
  div = -(-num1 // num2)
  return div

def binary_search(search_range, max_num, logs):
  search_min = 1
  search_max = search_range
  # 二分探索
  while True:
    # max_numを超えない最大回数にする
    count_a = 0
    # count_aより1短い長さ
    count_b = 0
    # 最小値と最大値の中間の値を出す
    half_num = (search_min + search_max - 1) // 2 + 1
    for i in range(logs):
      # 木を切る回数は(⌈(木の長さ)//(切りたい長さ)⌉-1)回
      count_a += round_up_division(A[i], half_num) - 1
      if half_num != 1:
        count_b += round_up_division(A[i], half_num - 1) - 1
    if count_a > K:
      # 多ければ長い半分で探索
      search_min = round_up_division(search_min + search_max, 2)
    elif half_num != 1 and count_b <= K:
      # 少なければ短い半分で探索
      search_max = half_num - 1
    else:
      # count_aが最大になれば終了
      return half_num
      break

N, K = map(int, input().split())
A = list(map(int, input().split()))
length_max = binary_search(max(A), K, N)
print(length_max)