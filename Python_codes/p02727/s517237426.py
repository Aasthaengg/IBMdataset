import sys
input = sys.stdin.readline

X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

C = p[:X] + q[:Y] + r
C.sort(reverse=True)

print(sum(C[:X+Y]))