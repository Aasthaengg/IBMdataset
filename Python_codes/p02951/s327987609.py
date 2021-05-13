# 初期入力
import sys
input = sys.stdin.readline
A,B,C = (int(x) for x in input().split())
C_residue =C-(A-B)
if 0 <=C_residue:
    print(C_residue)
else:
    print(0)