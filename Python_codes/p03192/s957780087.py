from sys import stdin

def solve() :
    N = stdin.readline().rstrip()
    ans = 0
    for x in N:
        if(x == "2") :
            ans += 1

    print(ans)
solve();