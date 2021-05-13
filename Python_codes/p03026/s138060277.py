import sys,math,collections,itertools
input = sys.stdin.readline

#大きいものから適当に決める。
#総和は最大数を除いた和になる選び方ができる。
#適当に最大数を置いて、周囲に大きい数字から順に置いていく
#BFSかな
N = int(input())
road = [[] for _ in range(N+1)]#1~N番までの道
number = [0]*(N+1)#indexに置く数字のメモ。BFSでは0なら行き先追加
for _ in range(N-1):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)
c = list(map(int,input().split()))

q = collections.deque([])
cSort=sorted(c)
number[1]=cSort.pop()
q.append(1)

while q:
    now = q.popleft()
    for idx in road[now]:
        if number[idx]==0:
            q.append(idx)
            number[idx]=cSort.pop()
print(sum(number[2:]))
print(*number[1:])
    
