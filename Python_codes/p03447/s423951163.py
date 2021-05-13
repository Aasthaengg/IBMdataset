# 初期入力
import sys
input = sys.stdin.readline
X = int(input())
A = int(input())
B = int(input())
ans =X-A
num_b =ans//B
ans = ans - num_b *B
print(ans)