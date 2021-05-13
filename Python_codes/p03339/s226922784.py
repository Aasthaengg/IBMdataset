
url = "https://atcoder.jp//contests/abc098/tasks/arc098_a"

def main():
    input()
    s = input()
    w_count = s.count('W')
    right_we = {"W": w_count, "E": len(s) - w_count}
    left_we = {"W": 0, "E": 0}
    ans = 10000000
    for v in s:
        right_we[v] -= 1
        ans = min(ans, right_we["E"] + left_we["W"])
        left_we[v] += 1
    print(ans)

if __name__ == '__main__':
    main()
