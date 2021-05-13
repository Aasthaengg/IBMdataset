import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b, k = map(int, input().split())
    ans = set()
    for i in range(k):
        if a + i + 1 <= b: ans.add(a + i)
        if b - i >= a: ans.add(b - i)
    ans = list(ans)
    ans.sort()
    for x in ans: print(x)

if __name__ == "__main__":
    main()
