s0 = input()
def convert(n, m):
  ans = ""
  while n > 0:
    amari = n % m
    ans += str(amari)
    n //= m
  return ans
n = len(s0) - 1
SUM = int(s0)
for i in range(1, 2**n):
  s1 = " ".join(list(s0))
  i = convert(i, 2)
  list_index = []
  for j in range(len(i)):
    list_index.append(i.find("1", j))
  list_index = list(set([x for x in list_index if x != -1]))
  for k in list_index:
    s1 = s1[:2*k+1] + "+" + s1[2*(k+1):]
  s1 = s1.replace(" ", "")
  sum_list = list(map(int, s1.split("+")))
  SUM += sum(sum_list)
print(SUM)