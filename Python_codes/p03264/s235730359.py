K = int(input())

a = K // 2 # 偶数の数
b = a + 1 if K % 2 != 0 else a

print(a * b)
