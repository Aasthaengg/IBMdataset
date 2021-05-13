from sys import stdin, stdout

int_in = lambda: int(stdin.readline())
arr_in = lambda: [int(x) for x in stdin.readline().split()]
mat_in = lambda rows: [arr_in() for y in range(rows)]
str_in = lambda: stdin.readline().strip()
out = lambda o: stdout.write("{}\n".format(o))
arr_out = lambda o: out(" ".join(map(str, o)))
bool_out = lambda o: out("YES" if o else "NO")
tests = lambda: range(1, int_in() + 1)


def solve(n, a, b):
    if abs(a-b) % 2 == 0:
        return abs(a-b) // 2

    down_ops = min(a, b)
    up_ops = n - max(a, b) + 1

    if down_ops < up_ops:
        return solve(n, 1, max(a, b) - down_ops) + down_ops

    return solve(n, min(a, b) + up_ops, n) + up_ops


if __name__ == "__main__":
    n, a, b = arr_in()
    out(solve(n, a, b))