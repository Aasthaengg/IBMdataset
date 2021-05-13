# ####################################################################
# import io
# import sys

# _INPUT = """\
# 2 3 -10
# 1 2 3
# 3 2 1
# 1 2 2
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
N,M,C = map(int, input().split())
B = [int(i) for i in input().split()]
AA = [[int(i) for i in input().split()] for _ in range(N)]

p(B)
p(AA)

ans = 0
for A in AA:
  x = C
  for a,b in zip(A,B):
     x += a * b

  if x > 0: ans += 1

print(ans)



