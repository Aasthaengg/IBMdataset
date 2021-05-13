import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
li = [A*N, B]
print(min(li))