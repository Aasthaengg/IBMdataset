import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
L = LI()
s = sum(L)
m = max(L)
print('Yes' if m < s-m else 'No')
