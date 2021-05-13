#料理が2個の時を考え、どちらを取れば良いか考える　これで得られた基準でソート
import sys
input = sys.stdin.readline

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda k: k[0]+k[1], reverse=True)
takahashi, aoki = 0, 0

for i in range(N):
    if i%2==0:
        takahashi += AB[i][0]
    else:
        aoki += AB[i][1]

print(takahashi-aoki)