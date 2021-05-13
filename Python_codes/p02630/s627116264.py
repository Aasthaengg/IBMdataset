import sys
input = sys.stdin.readline
N = int(input())
A = tuple(map(int,input().split()))
Q = int(input())
cnt = [0]*100005
s = sum(A)
for i in A:
    cnt[i] += 1
for i in range(Q):
    B, C = map(int,input().split())
    s += (C-B)*cnt[B]
    print(s)
    cnt[C] += cnt[B]
    cnt[B] = 0