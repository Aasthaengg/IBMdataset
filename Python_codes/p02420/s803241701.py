from collections import deque

def main():
    while True:
        try:
            S = input()
            M = int(input())
            H = tuple(int(input()) for _ in range(M))
        except EOFError:
            break

        s = deque(S)
        for h in H:
            s.rotate(-h)

        print(*s, sep='')

main()