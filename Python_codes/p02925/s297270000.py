#ABC139-E League
"""
全試合を頂点として、試合の順序を、先にやる試合→後にやる試合
で辺を張る。この時、後にやる試合の入次数を保持する。
入次数が0である試合は、それより前にやる試合が無いと言えるので、そのような試合から行っていく。
その頂点から出ている辺の入次数を-1する。
これを繰り返した結果、全試合(n(n-1)/2)が行えていればかかった日数を、
そうでないなら-1を出力する。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
edge = [[] for _ in range(2*(10**6))] #桁ずらしで管理。
dim_in = [-1]*(2*(10**6)) #-1のままなら、使われなかったことになる
dig = 10**3
for i in range(n):
    lst1 = list(map(int,readline().split()))
    fr = None
    for j in lst1:
        go = max(i,j-1) + min(i,j-1)*dig
        if fr != None:
            if dim_in[fr] < 0:
                dim_in[fr] = 0
            if dim_in[go] < 0:
                dim_in[go] = 0
            edge[fr].append(go)
            dim_in[go] += 1
        fr = go

#初日に行える試合を求める
can_game = []
count = 0
for idx,i in enumerate(dim_in):
    if i == 0:
        count += 1
        can_game.append(idx)

day = 0
while len(can_game) > 0:
    next_game = []
    for i in can_game:
        for j in edge[i]:
            dim_in[j] -= 1
            if dim_in[j] == 0:
                count += 1
                next_game.append(j)
    can_game = next_game
    day += 1

if count >= n*(n-1)//2:
    print(day)
else:
    print(-1)