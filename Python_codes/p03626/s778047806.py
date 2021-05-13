import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    N = int(input())
    S1 = input()
    S2 = input()
    cut = []
    pre = None
    for i, c in enumerate(S1):
        if c != pre: cut.append(i)
        pre = c
    cut.append(N)
    ans = 1
    l = len(cut)
    pre = True  # vertical domino
    for i in range(l - 1):
        if i == 0 and cut[1] - cut[0] == 1:
            ans = 3
            pre = True
            continue
        if i == 0 and cut[1] - cut[0] == 2:
            ans = 6
            pre = False
            continue
        if pre and cut[i + 1] - cut[i] == 1:
            ans *= 2
            pre = True
        elif pre:
            ans *= 2
            pre = False
        elif not pre and cut[i + 1] - cut[i] == 1:
            pre = True
        else:
            ans *= 3
            pre = False
        ans %= mod
    print(ans)
    

if __name__ == "__main__":
    main()
