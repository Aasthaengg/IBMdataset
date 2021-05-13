import sys
from collections import deque

def main():
    A = deque()
    input()
    for e in sys.stdin:
        if e[0]=='i': #insert xxx
            A.appendleft(e[7:-1])
        else:
            if e[6]==' ': #delete xxx
                m = e[7:-1]
                if m in A: 
                    A.remove(m)
            elif e[6]=='F':
                A.popleft()
            else:
                A.pop()
    print(' '.join(A))

if __name__=='__main__':
    main()
