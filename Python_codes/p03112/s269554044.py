import bisect
import sys
input = sys.stdin.readline

A,B,Q = map(int,(input().split()))
s = [[0]*3 for _ in range(A)]
t = [[0]*3 for _ in range(B)]
x = [[0]*3 for _ in range(Q)]
slen = []
tlen = []
road = []
for i in range(A):
    s[i][0] = int(input())
    slen.append(s[i][0])
    s[i][1] = "s"
    road.append(s[i])
for i in range(B):
    t[i][0] = int(input())
    tlen.append(t[i][0])
    t[i][1] = "t"
    road.append(t[i])
for i in range(Q):
    x[i][0] = int(input())
road.sort()

for i in range(len(s)):
    index = bisect.bisect_left(tlen,s[i][0])
    if index < B:
        s[i][2] = min(abs(s[i][0]-tlen[index-1]),abs(tlen[index]-s[i][0]))
    else:
        s[i][2] = abs(s[i][0]-tlen[index-1])
for i in range(len(t)):
    index = bisect.bisect_left(slen,t[i][0])
    if index < A:
        t[i][2] = min(abs(t[i][0]-slen[index-1]),abs(slen[index]-t[i][0]))
    else:
        t[i][2] = abs(t[i][0]-slen[index-1])

for i in range(Q):
    index = bisect.bisect_left(road,x[i])
    if index < A+B:
        print(min(abs(x[i][0]-road[index-1][0])+road[index-1][2],abs(x[i][0]-road[index][0])+road[index][2]))
    else:
        print(abs(x[i][0]-road[index-1][0])+road[index-1][2])