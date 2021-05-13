n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sA = sum(a)
sB = sum(b)

# Ai ≤ Bi: Ai++ができるので，問題なし
#  - このとき (Bi - Ai) // 2回数は j として選んでOK
#
# Ai > Bi: i以外を選んで，Biを嵩上げする必要がある
# - 選んだjは A[j] + 2 ≤ B[j] が必要
# - Biは1ずつしか増えないので，これは-d回必要
#


diff = [b[i] - a[i] for i in range(n)]
count = 0
for d in diff:
    if d > 0: # Ai ≤ Bi
        count += d // 2  # 余る分
    else:     # Ai ≥ Bi
        count -= -d      # 嵩上げ

# 余る分が多ければ，嵩上げできる
if count >= 0:
    print("Yes")
else:
    print("No")