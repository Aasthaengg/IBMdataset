#値を入力
n = int(input())
s = []
for i in range(n):
  s.append(input())

m = int(input())
t = []
for i in range(m):
  t.append(input())

#sに含まれる文字列個数を辞書にカウント
dic = {}

for i in range(n):
  if s[i] not in dic:
    dic[s[i]] = 0
  dic[s[i]] += 1

#tの文字列の中で、sにも含まれている文字列の引き算だけ行う
for i in range(m):
  if t[i] in dic:
    dic[t[i]] -= 1

#辞書の最大値あるいは0のうち大きい方が答え
max_dic = max(max(dic.values()), 0)

print(max_dic)