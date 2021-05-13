import sys
def I(): return int(sys.stdin.readline().rstrip())

N,K,X,Y = I(),I(),I(),I()
print(min(K,N)*X + (max(K,N)-K)*Y)
