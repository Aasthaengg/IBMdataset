import sys

read= sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 1000000007
sys.setrecursionlimit(10**7)

#N,*A = map(int,read().split())
N = int(input())
l = list(map(int,input().split()))

#最初の状態分を加算するため、1からカウント
ans = 1

S = 0 #現在の状態 増加 or 減少 or 初期化

for i in range(1,N):
    X = l[i] - l[i-1]

    X = 0 if X == 0 else 1 if X > 0 else -1

    #同じ値の時l[i] == l[i-1]
    if X == 0:
        continue

    #Stateが初期のときは現在の状態に更新
    elif S == 0:
        S = X

    #Stateが違うときは答えに加算して、Stateを初期値に
    elif S != X:
        ans += 1
        S = 0

print(ans)
