arr = list(int(a) for a in input().split())

# 最小値ベースに直して
# ２つ選んで２減らす
# １つ選んで１減らす

arr.sort()
A = 0
B = arr[1] - arr[0]
C = arr[2] - arr[0]

# 2で何回割り切れるか
ans = B // 2

# 残りがいくつあるか
B -= ans * 2
C -= ans * 2
ans += B + C

print(ans)
