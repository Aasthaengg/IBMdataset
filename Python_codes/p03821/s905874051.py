import sys
input = sys.stdin.readline
N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]   
cnt = 0
for i in range(N-1,-1,-1):
    if (AB[i][0]+cnt)%AB[i][1] == 0:
        continue
    else:
        cnt += AB[i][1] - (AB[i][0]+cnt)%AB[i][1]
print(cnt)
