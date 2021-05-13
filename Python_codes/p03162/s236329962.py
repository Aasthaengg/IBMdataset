N = int(input().rstrip())
judge = []
for _ in range(N):
  hap_lst = list(map(int, input().rstrip().split(' ')))
  if not judge:
    judge = hap_lst
  else:
    a_0, b_0, c_0 = judge
    a_1, b_1, c_1 = hap_lst
    judge = [a_1 + max(b_0, c_0), b_1 + max(a_0, c_0), c_1 + max(a_0, b_0)]
print(max(judge))
