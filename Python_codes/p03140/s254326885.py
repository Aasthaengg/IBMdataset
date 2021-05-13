import sys
def main():
    input = sys.stdin.read
    N,A,B,C=input().rstrip().split()
    ans = 0
    for S in zip(A,B,C):
        s = len(set(S))
        if s == 3: ans += 2
        elif s == 2: ans += 1
    print(ans)

if __name__ == '__main__':
    main()