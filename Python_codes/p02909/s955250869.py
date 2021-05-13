import sys

def solve():
    input = sys.stdin.readline
    S = input().strip("\n")
    if S[0] == "S": print("Cloudy")
    elif S[0] == "C":print("Rainy")
    else: print("Sunny")
    return 0

if __name__ == "__main__":
    solve()