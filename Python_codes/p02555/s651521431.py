S = int(input())
count = 0
for size in range(1, S//3+1):
  extra = S - 3 * size # 0以上の値をどう分配するか？数列なので純不動ではない
  total = extra + size -1 # extra個の玉とsize-1個の棒の並び替え問題
  number = 1
  for n in range(extra+1, total+1):
    number *= n
  for n in range(1, size):
    number //= n
  count += number
#  print(size,number)
print(count % (10 ** 9 + 7))