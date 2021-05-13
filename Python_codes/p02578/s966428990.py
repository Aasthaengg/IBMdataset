def solve(n,arr):
    maxh = 0
    h = 0
    for i in range(1,n):
        curr = arr[i]
        curh = arr[i-1]
        f = max(curr,curh)
        maxh = max(f,maxh)

        if curr < maxh:
            h += maxh - curr

        # print(f"curr:{curr},curh:{curh},maxh:{maxh}")
        # print(f"h:{h}")

    return h
        



n = int(input())
arr = list(map(int, input().strip().split()))

print(solve(n,arr))