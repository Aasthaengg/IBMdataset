import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    A, B, T = input_nums()
    time = 0
    total = 0
    while True:
        time += A
        if time > T +0.5: break
        total += B
    print(total)
if __name__ == '__main__':
    main()
