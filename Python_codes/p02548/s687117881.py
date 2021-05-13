import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
print(sum((N-1)//i for i in range(1,N)))

# 対称性を利用して、計算量を O(N**.5) にすることも可能
