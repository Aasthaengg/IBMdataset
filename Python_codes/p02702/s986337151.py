import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import defaultdict 
def main():
    s = readline().rstrip().decode()
    n = len(s)
    T = [0]
    P = 2019
    dd = defaultdict(int)
    dd[0] += 1
    for i in range(1, n+1):
        v = ((ord(s[-i])-ord('0'))*pow(10, i-1, P) + T[i-1])%P
        dd[v] += 1
        T.append(v)
    ans = 0
    for v in dd.values():
        ans += v*(v-1)//2
    print(ans)
if __name__ == '__main__':
    main()
