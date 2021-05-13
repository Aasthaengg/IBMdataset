import sys
input = sys.stdin.readline
from collections import deque
def main():
    X = list(input().rstrip())
    past = deque()
    cnt = 0
    last = X[0]
    for i in range(1,len(X)):
        if last + X[i] == 'ST':
            if len(past) > 0:
                last = past.pop()
            else:
                last = ''
            cnt += 2
        else:
            past.append(last)
            last = X[i]
    print(len(X) - cnt)
        
if __name__ == '__main__':
    main()