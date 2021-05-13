#ABC 055C Scc Puzzle
import sys
N, M = map(int, sys.stdin.readline().split())

#print(N, M)

cnt = min(N, M//2)
N -=cnt
M-=2*cnt

cnt +=M//4
print(cnt)