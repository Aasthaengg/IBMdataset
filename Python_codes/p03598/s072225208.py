# ####################################################################
# import io
# import sys

# _INPUT = """\
# 84 97 66
# 79 89 11
# 61 59 7
# 7
# 89
# 7
# 87
# 79
# 24
# 84
# 30

# """
# sys.stdin = io.StringIO(_INPUT)
####################################################################
import sys
def p(*_a):
  # return
  _s=" ".join(map(str,_a))
  #print(_s)
  sys.stderr.write(_s+"\n")
####################################################################
yn = lambda b: print('Yes') if b else print('No')
####################################################################
N = int(input())
K = int(input())
X = [int(i) for i in input().split()]

ans = 0
for x in X:
  ans += min(x, abs(K-x)) * 2

print(ans)
