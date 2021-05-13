#AGC035-A XOR Circle
"""
問題：
円環状にリストの数値を配置した時、aのどの要素についても
ai == a(i-1)^a(i+1)
となるように配置できるか判定せよ
解法：
できるかどうかを判定すればよいので実際に組み立てる必要はない。
n<=10**5であることから、選び方を考えなくて良い解法が存在するはず
全てのXORの合計が0?
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))

ans = 0
for i in lst1:
    ans = ans^i

print("Yes" if ans == 0 else "No")