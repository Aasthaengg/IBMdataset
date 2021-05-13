import sys,math,collections,itertools
input = sys.stdin.readline

H,W=list(map(int,input().split()))
s = [ input().rstrip() for _ in range(H)]
dp = [[0]*W for _ in range(H)]

def isOK(start):
    q =  collections.deque([start])
    dp[start[0]][start[1]] = 1
    black,white=0,0
    while q:
        nowh,noww = q.popleft()
        if s[nowh][noww] == '.':
            target_mark = '#'
            white +=1
        else:
            target_mark = '.'
            black +=1
        if nowh >0 and s[nowh-1][noww] == target_mark and dp[nowh-1][noww]==0:
            q.append((nowh-1,noww))
            dp[nowh-1][noww]=1
        if nowh <H-1 and s[nowh+1][noww] == target_mark and dp[nowh+1][noww]==0:
            q.append((nowh+1,noww))
            dp[nowh+1][noww]=1
        if noww > 0 and s[nowh][noww-1] == target_mark and dp[nowh][noww-1]==0:
            q.append((nowh,noww-1))
            dp[nowh][noww-1]=1
        if noww < W-1 and s[nowh][noww+1] == target_mark and dp[nowh][noww+1]==0:
            q.append((nowh,noww+1))
            dp[nowh][noww+1]=1
            
    return black*white

cnt = 0

start_candi = []
end_candi = []
for ih in range(H):
    for iw in range(W):
        if s[ih][iw] == '#':
            start_candi.append((ih,iw))
        else:
            end_candi.append((ih,iw))

for ih in range(H):
    for iw in range(W):
        if dp[ih][iw] == 0:
            start = (ih,iw)
            cnt += isOK(start)
        else:
            continue

print(cnt)
