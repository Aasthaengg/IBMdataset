import sys
from pprint import pprint

def solve(a, b, c):
    if a == b == c:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':

    a, b, c = sys.stdin.readline().strip().split(" ")
    ans = solve(int(a), int(b), int(c))
    print ans