a = int(input())
num_list = list(map(int,input().split()))

#考えられるすべての組み合わせを計算
total = 3**a

#奇数になるパターンを計算
cul_list = [j for j in range(a)]
for i in range(a):
  if num_list[i] % 2 == 0:
    cul_list[i] = 2
  else:
    cul_list[i] = 1
#print(cul_list)
ans = 1
for k in cul_list:
  ans *= k
print(total - ans)