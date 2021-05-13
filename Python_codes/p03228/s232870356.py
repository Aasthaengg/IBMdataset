import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


A, B, K = mi()

for i in range(K):
    if i % 2 == 0:
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A //= 2
    else:
        if B % 2 == 1:
            B -= 1
        A += B // 2
        B //= 2

print(A, B)
