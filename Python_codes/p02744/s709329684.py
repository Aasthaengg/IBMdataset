def solve(ans, p, n):
    if len(p) == n:
        s = ""
        for v in p:
            s += chr(ord("a")+v)
        ans.append(s)
        return
    for v in range(max(p)+2):
        p.append(v)
        solve(ans, p, n)
        p.pop()
    return

def main():
    n = int(input())
    ans = []
    p = [0]
    solve(ans, p, n)
    ans.sort()
    for v in ans:
        print(v)

if __name__ == "__main__":
    main()