# coding-utf8 #

a = int(input())
b = int(input())
c = int(input())
x = int(input())

# 全探索
# 全部0枚から初めてそれぞれの硬貨枚数までインクリメントしていって、
# ちょうどx円になるものを探す

count = 0

for i_500 in range(a + 1):
  for i_100 in range(b + 1):
    for i_50 in range(c + 1):
      sum = 500 * i_500 + 100 * i_100  + 50 * i_50
      if sum == x:
        count += 1

print(count)