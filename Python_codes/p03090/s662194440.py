#AGC032-B Balanced Neighbors
"""
まずnが偶数の場合を考える。
1...nの数列を考えた時に、
1+n,2+n-1,3+n-2…を１頂点として考えると、全てその値が等しいグラフになる。
次に奇数の場合を考える。
n-1までのグラフを偶数の場合と同じように構築した後、
nはn-1までの2頂点の合計と等しい値になる。
よって、最後に全頂点をnとつなぎ合わせると条件を満たすグラフに成る。
"""
import sys
from collections import defaultdict
dic1 = defaultdict(int)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
ans = []
mid = 1+(n//2)*2
for i in range(1,(n//2)*2+1):
    dic1[i] = mid-i
for i in range(1,(n//2)*2):
    res = dic1[i]
    for j in range(i+1,(n//2)*2+1):
        if j == res:
            continue
        ans.append([i,j])

if not even(n):
    for i in range(1,n):
        ans.append([i,n])

print(len(ans))
for i in ans:
    print(*i)
