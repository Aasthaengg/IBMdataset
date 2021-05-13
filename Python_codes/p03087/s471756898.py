import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, q = map(int, input().split())
    s = list(input())
    lr = [list(map(int, input().split())) for _ in range(q)]
    ac = [0] * len(s)
    for i in range(1, len(s)):
        if s[i-1]=='A' and s[i]=='C':
            ac[i] = ac[i-1] + 1
        else:
            ac[i] = ac[i-1]
    for i in lr:
        print(ac[i[1]-1]-ac[i[0]-1])
            
if __name__ == '__main__':
    main()