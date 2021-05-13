from sys import stdin, stdout

int_in = lambda: int(stdin.readline())
arr_in = lambda: [int(x) for x in stdin.readline().split()]
mat_in = lambda rows: [arr_in() for y in range(rows)]
str_in = lambda: stdin.readline().strip()
out = lambda o: stdout.write("{}\n".format(o))
arr_out = lambda o: out(" ".join(map(str, o)))
bool_out = lambda o: out("YES" if o else "NO")
tests = lambda: range(1, int_in() + 1)


def solve(h, w, matrix):
    dp = [[[0, False] for x in range(w)] for y in range(h)]
    for row in range(h):
        for col in range(w):
            dp[row][col][1] = matrix[row][col] == "#"
            prev = False
            if row > 0 and col > 0:
                if dp[row-1][col][0] < dp[row][col-1][0]:
                    prev = dp[row-1][col][1]
                    dp[row][col][0] = dp[row-1][col][0]
                elif dp[row-1][col][0] > dp[row][col-1][0]:
                    prev = dp[row][col-1][1]
                    dp[row][col][0] = dp[row][col-1][0]
                else:
                    prev = dp[row-1][col][1] or dp[row][col-1][1]
                    dp[row][col][0] = dp[row][col-1][0]
            elif row > 0:
                prev = dp[row-1][col][1]
                dp[row][col][0] = dp[row-1][col][0]
            elif col > 0:
                prev = dp[row][col-1][1]
                dp[row][col][0] = dp[row][col-1][0]
            if dp[row][col][1] and not prev:
                dp[row][col][0] += 1
    return dp[h-1][w-1][0]


if __name__ == "__main__":
    h, w = arr_in()
    matrix = [str_in() for x in range(h)]
    out(solve(h, w, matrix))