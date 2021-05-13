import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    S = input()
    if S[0] != 'A' or ord('A') <= ord(S[1]) <= ord('Z') or ord('A') <= ord(S[-1]) <= ord('Z'):
        print("WA")
        return
    capital = []
    for i in range(2, len(S) - 1):
        if ord('a') <= ord(S[i]) <= ord('z'): continue
        capital.append(S[i])
    
    if capital == ['C']:
        print("AC")
    else:
        print("WA") 


if __name__ == "__main__":
    main()
