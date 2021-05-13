def solve():
    N = int(input())
    ans = ['a']
    for i in range(N - 1):
        newest_ans = []
        for a in ans:
            A = [ord(b) for b in a]
            for t in range(min(A), max(A) + 2):
                newest_ans.append(a + chr(t))
        ans = newest_ans
    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    solve()