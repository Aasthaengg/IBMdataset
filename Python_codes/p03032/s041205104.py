import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))
from collections import deque

def main():
    N, K = input_nums()
    V = input_nums()
    maxv = 0
    for total in range(min(N, K)+1):
        for a in range(total+1):
            D = deque(V)
            gems = []
            b = total - a
            for i in range(a):
                gems.append(D.pop())
            for i in range(b):
                gems.append(D.popleft())
            gems.sort(reverse=True)
            d = K - (a+b)
            for i in range(d):
                if len(gems) > 0:
                    a = gems.pop()
                    if a < 0:
                        continue
                    else:
                        gems.append(a)
                        break
            maxv = max(maxv, sum(gems))
    print(maxv)

if __name__ == '__main__':
    main()
