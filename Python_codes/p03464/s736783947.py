k = int(input())
a = list(map(int, input().split()))
def solve():

    if a[k-1] != 2:
        print(-1)
        return

    mi = 2
    mx = 2

    for i in range(k):
        j = k-i-1

        mx = mx + a[j] - 1

        if j == 0:
            pass
        else:
            na = a[j-1]
            
            if mx % na != 0 and mi % na != 0 and ((mx % na) - (mi % na)) == (mx - mi):
                print(-1)
                return

            if mi%na != 0:
                mi = mi + (na - mi%na)

            if mx%na != 0:
                mx = mx - (mx % na)

    print(mi, mx)
solve()
