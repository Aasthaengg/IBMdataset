from sys import stdin

A, B, = [int(x) for x in stdin.readline().rstrip().split()]  # 空白区切り
ANS = max(A + B, A - B, A * B)
print(ANS)
