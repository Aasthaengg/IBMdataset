N, C = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
SV = [0]
for x, v in S:
    SV.append(v+SV[-1])
left = [0]
leftturn = [0]
for i in range(N):
    left.append(SV[i+1]-S[i][0])
    leftturn.append(SV[i+1]-S[i][0]*2)
S.reverse()
SV = [0]
for x, v in S:
    SV.append(v+SV[-1])
right = [0]
rightturn = [0]
for i in range(N):
    right.append(SV[i+1]-(C-S[i][0]))
    rightturn.append(SV[i+1]-(C-S[i][0])*2)
ml = [0]
mr = [0]
mlt = [0]
mrt = [0]
for i in range(N):
    ml.append(max(left[i+1], ml[-1]))
    mr.append(max(right[i+1], mr[-1]))
    mlt.append(max(leftturn[i+1], mlt[-1]))
    mrt.append(max(rightturn[i+1], mrt[-1]))
res = 0
for i in range(N+1):
    res = max(res, ml[i]+mrt[N-i], mr[i]+mlt[N-i])
print(res)
