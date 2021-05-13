h1, m1, h2, m2, k = map(int, input().split())
 
# 時間を、0時0分からの経過時間に変換する。
start = (60 * h1) + m1
end = (60 * h2) + m2 - k
 
print(end - start)