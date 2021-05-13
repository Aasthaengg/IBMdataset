import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    l = len(s)
    ans = l - 2
    for i in range(2, l):
        if i % 2 != 0: continue
        ns = s[:l-i]
        even = True
        for j, c in enumerate(ns):
            if j >= (l - i) // 2: break
            if c != ns[(l - i) // 2 + j]:
                even = False
                break
        if even:
            ans = l - i
            break
    print(ans)


if __name__ == "__main__":
    main()
