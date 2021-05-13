import sys

input = sys.stdin.readline


class AtCoder:
    def main(self):
        N, A, B = map(int, input().split())
        if abs(A - B) % 2 == 1:
            print('Borys')
        else:
            print('Alice')


# Run main
if __name__ == '__main__':
    AtCoder().main()
