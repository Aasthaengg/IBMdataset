
def ask(i):
    print(i)
    return input()

def solve(l, r):
    m = (l + r) // 2
    res = ask(m)
    if res == "Vacant":
        quit()
    if (m % 2 == 0 and a0 == res) or (m % 2 == 1 and a0 != res):
        solve(m + 1, r)
    else:
        solve(l, m)

N = int(input())
a0 = ask(0)
if a0 == "Vacant":
    quit()
solve(1, N)
