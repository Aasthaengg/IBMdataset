from sys import stdin

A, B, C, D = [int(x) for x in stdin.readline().rstrip().split()]  # 空白区切り

if abs(A - C) <= D or (abs(A - B) <= D and abs(B - C) <= D):
    print("Yes")
else:
    print("No")
