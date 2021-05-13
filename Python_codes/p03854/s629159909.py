from collections import deque
import sys

def fnw(n,s):
    sm=deque([])
    if n<=len(s):
        for _ in range(n):
            sm.append(s.popleft())
    return sm

def jfws(s):
    # print(s)
    sm=fnw(5,s)
    # print(sm)
    if ''.join(sm)=='dream':
        sm=fnw(2,s)
        if ''.join(sm)=='er':
            if bool(s):
                if s[0]=='a':
                    s.extendleft(deque(reversed(list(sm))))
        else:
            s.extendleft(deque(reversed(list(sm))))
        return False
    elif ''.join(sm)=='erase':
        sm=fnw(1,s)
        if ''.join(sm)!='r':
            s.extendleft(sm)
        return False
    else:
        return True 

def main(s):
    while len(s)>0:
        if jfws(s):
            return 'NO'
    return 'YES'

s=deque(sys.stdin.readline().strip())
print(main(s))

