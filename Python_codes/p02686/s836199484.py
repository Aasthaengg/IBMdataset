import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def end(flag):
    if flag:
        print('Yes')
    else:
        print('No')
    exit(0) #プログラムを終了

n = int(input())
plus = []
minus = []
zero = []
total = 0
for i in range(n):
    s = input()[:-1] #入力の右端の値を除去
    cnt = 0
    M = 0
    m = 0
    for t in s:
        if t == ')': #前から探索
            cnt += 1
            # print('+cnt:{}'.format(cnt))
            M = max(M,cnt) #'('が多い場合はcnt=0,')'が多い場合はcntは'('と')'の個数の差
            # print('M:{}'.format(M))
        else:
            cnt -= 1
            # print('-cnt:{}'.format(cnt))
    cnt = 0
    for t in s[::-1]: #後ろから探索
        if t == ')':
            cnt += 1
            # print('+cnt:{}'.format(cnt))
        else:
            cnt -= 1
            # print('-cnt:{}'.format(cnt))
            m = min(m,cnt) #')'が多い場合はcnt=0,'('が多い場合はcntは'('と')'の個数の差
            # print('m:{}'.format(m))
    if cnt > 0:
        minus.append((-m,cnt))
    elif cnt == 0:
        zero.append((-m,M))
    else:
        plus.append((M,-cnt))
    S = (M,-cnt)
    total += cnt
if total != 0:
    end(0)
plus.sort()
minus.sort()
cnt = 0
for need,increase in plus:
    if cnt < need:
        end(0)
    else:
        cnt += increase
cnt = 0
for need,increase in minus:
    if cnt < need:
        end(0)
    else:
        cnt += increase
for m,M in zero:
    if m > cnt or M > cnt:
        end(0)
end(1)