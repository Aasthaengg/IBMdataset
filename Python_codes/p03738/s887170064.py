import sys

def solve():
    A = int(input())
    B = int(input())
    if A > B: print("GREATER")
    elif A < B: print("LESS")
    else: print("EQUAL")
            
    return 0

if __name__ == "__main__":
    solve()