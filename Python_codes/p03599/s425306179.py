import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    A,B,C,D,E,F = LI()

    w = set()
    for i in range(int(F/A/100)+1):
        for j in range(int(F/B/100)+1):
            if 0 < A*i+B*j <= int(F/100):
                w.add((A*i+B*j)*100)
    s = set()
    for i in range(int(F*E/(100+E)/C)+1):
        for j in range(int(F*E/(100+E)/D)+1):
            if 0 <= C*i+D*j <= int(F*E/(100+E)):
                s.add(C*i+D*j)

    max_E = -1.0
    ans_w = 0
    ans_s = 0
    for x in w:
        for y in s:
            if x + y <= F and y <= x/100 * E and max_E < y/(x+y) * 100:
                max_E = y/(x+y) * 100
                ans_w = x + y
                ans_s = y
    print(ans_w,ans_s)

if __name__ == '__main__':
    main()