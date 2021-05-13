import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main(): 
    s = input() + 'a'
    x,y = map(int,input().split())
    
    cnt_t = 0
    cnt_f = 0
    p = []
    q = []
    before = True
    for i in range(len(s)-1):
        if s[i] == 'T' :
            cnt_t += 1
        elif s[i] == 'F' and s[i+1] == 'F':
            cnt_f += 1
        else:
            cnt_f += 1
            if cnt_t == 0:
                x -= cnt_f
            elif cnt_t%2 == 0:
                if before:
                    p.append(cnt_f)
                else:
                    q.append(cnt_f)
            else:
                if before:
                    q.append(cnt_f)
                    before = False
                else:
                    p.append(cnt_f)
                    before = True
            cnt_t = 0
            cnt_f = 0
    
    
    p.sort(reverse=True)
    q.sort(reverse=True)

    s = 0
    for i in range(len(p)):
        if s <= x:
            s += p[i]
        else:
            s -= p[i]
    
    t = 0
    for i in range(len(q)):
        if t <= y:
            t += q[i]
        else:
            t -= q[i]
    
    if s == x and t == y:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()

