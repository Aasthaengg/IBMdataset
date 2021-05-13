# NOMURA プログラミングコンテスト 2020-A

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


H1,M1,H2,M2,K = MI()
print(max(0,60*H2+M2-60*H1-M1-K))
