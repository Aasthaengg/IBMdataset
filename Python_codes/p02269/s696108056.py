from sys import stdin

n = int(input())
set_ = set()

for _ in range(n):
    cmd, s = stdin.readline().split()

    if cmd == "insert":
        set_.add(s)
    if cmd == "find":
        ans = ["no", "yes"][s in set_]
        print(ans)

