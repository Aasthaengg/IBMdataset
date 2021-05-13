k = int(input())
a = k // 2
b = a if k % 2 == 0 else a + 1
ans = a * b
print(ans)