# 手持ちの金で、何回聞けるかを求める

A, B, C = map(int, input().split())

if C <= (B // A):
    print(C)
else:
    print(B // A)
