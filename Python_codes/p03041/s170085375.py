# 初期入力
import sys
input = sys.stdin.readline
N,K = (int(x) for x in input().split())
S =input().strip()
S_small=S.lower()
ans =S[:K-1] +S_small[K-1] +S[K:]
print(ans)