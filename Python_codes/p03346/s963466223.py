#AGC024-B Backfront
"""
ある一要素を選んで数列の先頭もしくは最後尾に移動させる。
これを繰り返して昇順に並び替えるときの最小手数
解法：
O(N)で求める必要があるので、シュミレーション的な解法ではない。
増加部分列のうち、その増加分が1である制約を加えた場合の
部分列の長さをlとした時、
n-lが答え。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(int(readline())-1)

lst2 = [0]*n
for i in range(n):
    lst2[lst1[i]] = i 
#lst2にlst1でのindex(場所)を保存した場合、
#左右の２要素について、右の要素が左より大きければ、
#その2要素については連続でその昇順に存在していることがわかる
#print(lst1)
#print(lst2)

ans = 0
res = 1
for i in range(1,n):
    if lst2[i] > lst2[i-1]:
        res += 1
    else:
        ans = max(ans,res)
        res = 1

ans = max(ans,res)
print(n-ans)