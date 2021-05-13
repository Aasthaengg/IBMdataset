import sys

def solve():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    print("Yes" if A <= C <= B else "No")
   
    
    return 0

if __name__ == "__main__":
    solve()