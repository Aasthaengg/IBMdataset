#AGC024-C Sequence Growing Easy
"""
問題：
lst1とlst2がある。
lst1の値が与えられ、lst2の値は最初全て0である。
lst2[i+1] = lst2[i]+1
を繰り返し、lst1と等しくできる場合その最小手数を出力せよ。

考察：
足し合わせる、ではなく、置き換える、なので、
必ずlst2[i+1] <= lst2[i] + 1となる。
左から最大に足し合わせた場合、
0 1 2 3 4...としかならない。
他に
0 0 1 0 0
0 0 1 2 0
0 0 1 2 3
0 1 1 2 3
0 1 2 2 3
0 1 2 3 3 (3+3で6手)
のような遷移も可能
0 0 0 1 0
0 0 0 1 2
0 1 0 1 2
0 1 2 1 2
0 1 2 3 2 (3+2で5手)
解法：
左からリストを見ていった時に、
必ずlst1[i+1] <= lst1[i] + 1となっていることを確認しながら、
正常な遷移でない部分の値を足し合わせることによって答えが求まる
正常でない遷移：↑のシュミレーションの3+3とか3+2の部分
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(int(readline()))
if lst1[0] != 0:
    print(-1)
    exit()
ans = 0
for i in range(n-1):
    if lst1[i]+1 == lst1[i+1]:
        continue
    if lst1[i]+1 < lst1[i+1]:
        print(-1)
        exit()
    if lst1[i] >= lst1[i+1]:
        ans += lst1[i]
print(ans+lst1[-1])