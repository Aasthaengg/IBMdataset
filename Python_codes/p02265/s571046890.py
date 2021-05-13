from collections import deque
import sys

def main():
    y = deque()
    input()
    for order in sys.stdin:
        if order[0] == "i":
            y.appendleft(order[7:-1])
        elif order[6] == " ":
            try:
                y.remove(order[7:-1])
            except:
                pass
        elif order[6] == "F":
            y.popleft()
        else:
            y.pop()
    print(" ".join(y))
    
if __name__ == "__main__":
    main()
