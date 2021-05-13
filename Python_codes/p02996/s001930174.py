import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    a_b = []
    for _ in range(n):
        a_b.append(LI())
    a_b.sort(key=lambda x: x[1])
    t = 0
    for d in a_b:
        t += d[0]
        if t > d[1]:
            print("No")
            sys.exit()
    print("Yes")

if __name__ == '__main__':
    main()