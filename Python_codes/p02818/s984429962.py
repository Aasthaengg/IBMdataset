A, B, K = map(int, input().split())
# 高橋A枚, 青木B枚, K回繰り返す

diffA = min(K, A)
A -= diffA
B -= min(B, K - diffA)

print(A, B)

