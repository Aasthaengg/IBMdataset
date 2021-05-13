N, M = map(int, input().split())

# 下の式はN=0,1(M=0,1)の場合も成り立つ
a = N*(N-1) // 2
b = M*(M-1) // 2
  
print(a+b)