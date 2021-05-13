import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines

def main():
    lines = input()

    n = int(lines[0].strip())
    a = list(map(int, lines[1].split()))

    a = sorted(a)
    c = a[n//2 - 1] ; d = a[n//2]

    print(d-c)

main()