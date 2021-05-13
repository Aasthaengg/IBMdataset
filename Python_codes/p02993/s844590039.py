# 初期入力
import sys
input = sys.stdin.readline
S =input().strip()
for i in range(len(S)-1):
    if S[i] ==S[i+1]:
        print("Bad")
        exit()
print("Good")