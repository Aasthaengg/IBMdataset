# ????????????????????°??????
import sys

def main():
    while True:
        m, f, r = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        if m == -1 and f == -1 and r == -1:
            break

        sum = m + f
        
        if m == -1 or f == -1:
            rank = 'F'
        elif sum >= 80:
            rank = 'A'
        elif sum >= 65:
            rank = 'B'
        elif sum >= 50:
            rank = 'C'
        elif sum >= 30:
            if r >= 50:
                rank = 'C'
            else:
                rank = 'D'
        else:
            rank = 'F'

        print(rank)

if __name__ == '__main__':
    main()