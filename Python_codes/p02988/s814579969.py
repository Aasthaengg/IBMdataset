import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines

def main():
    lines = input()
    n = int(lines[0].strip())
    a = list(map(int, lines[1].split()))

    cnt = 0

    for i in range(2, n):
        b = a[i-2:i+1]
        b = sorted(b)
        if a[i-1] == b[1]:
            cnt += 1

    print(cnt)

main()
