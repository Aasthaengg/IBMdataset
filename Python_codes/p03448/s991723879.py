a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())  # 500 * A + 100 * B + 50 * C

result = []
for a_i in range(a+1):
  for b_i in range(b+1):
    for c_i in range(c+1):
      x_tmp = x - 500 * a_i - 100 * b_i - 50 * c_i
      if x_tmp == 0:
      	result.append([a_i, b_i, c_i])
print(len(result))
