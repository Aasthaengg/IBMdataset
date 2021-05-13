import sys
input = sys.stdin.readline
n = 0

def main():
    n = int(input())
    D = sorted(map(int, input().split()))
    abc = D[:n//2]
    arc = D[n//2:]
    print(arc[0] - abc[-1])



main()
