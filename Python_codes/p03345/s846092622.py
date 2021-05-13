import sys
readline=sys.stdin.readline

A,B,C,K=map(int,readline().split())

# B+x,B,C
# B+C,B+C+x,2B+x
# 3B+C+2x,3B+c+x,2B+2C+x

# 奇数回実行すると答えは-x、偶数回だとx

print((A-B)*(-1)**(K&1))