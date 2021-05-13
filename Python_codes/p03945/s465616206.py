import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    pre = S[0]
    ans = 0
    for i, c in enumerate(S):
        if i == 0: continue
        if c != pre:
            ans += 1
            pre = c
    print(ans)

if __name__ == "__main__":
    main()
