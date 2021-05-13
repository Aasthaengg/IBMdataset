import sys
from collections import deque
def input(): return sys.stdin.readline().strip()

def main():
    a = deque(input())
    b = deque(input())
    c = deque(input())
    d = {'a': a, 'b': b, 'c': c}
    turn = 'a'
    while d[turn]:
        turn = d[turn].popleft()
    print(str.upper(turn))



if __name__ == "__main__":
    main()
