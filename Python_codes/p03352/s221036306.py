X = int(input())

# Xは1000以下なので、pは2**10=1024より10まで探索すれば十分
# 同様にbは40程度まで考えれば十分
max_ex = 1
for p in range(2, 10):
  for b in range(1, 40):
    if max_ex < b**p <= X:
      max_ex = b**p
      
print(max_ex)