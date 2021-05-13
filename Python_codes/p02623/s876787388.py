N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
from itertools import accumulate
accumulated1 = [0] + list(accumulate(A))
accumulated2 = [0] + list(accumulate(B)) + [10**10]
def check(x,now):
    if accumulated1[now] + accumulated2[x] <= K: return True
    else: return False

# [True, .. ,True ,False,.. , False ] のときは探索区間を半開区間で持つ
#[l,r)

def bisect(l,r,now):
    if r - l == 1: return  l
    mid = (r+l)//2
    # l <= r ならば自明に l <= mid <= r  でこれの仮定は呼び出し1,2のいずれでも成立するので始めの呼び出しさえ正しければ永遠に成立.

    # //2 するので mid * 2 == r + l  か  mid * 2 ==  r + l + 1 のどっちか

    # 引数が l == r って時あるか? 
    # いま引数 l, rが l < r として,次の呼び出し1,2を考える.

    # mid == r  <=>  r - l == 0 (仮定より無い)か r - l == 1 (始めのifでカットするので無い)
    # mid == l  <=>  r - l == 0 (仮定より無い)か l - r == 1 (l > r なので無い)

    # 結局 一番始めの呼び出しのl,rを l < r とすれば 
    # l < mid < r となりずーっと l < r が保たれる.
    # l != mid かつ mid != r だから 1,2のどっちを呼び出されても更新される(無限ループとはならない)のでそのうち r - l == 1 になって止まる.

    if check(mid,now):
        #呼び出し1
        return bisect(mid,r,now)
    else:
        #呼び出し2
        return bisect(l,mid,now)


ans = 0
for i in range(N+1):
    if accumulated1[i] > K: pass
    else: ans = max(ans,bisect(0,M+1,i) + i)
print(ans)

