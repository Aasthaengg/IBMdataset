import sys
 
N, K = map(int, sys.stdin.readline().split(" "))
L = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
print(sum(L[0:K]))