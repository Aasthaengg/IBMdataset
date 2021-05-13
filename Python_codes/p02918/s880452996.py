def solve(a,k):
    curr_char = a[0]
    curr_len = 0
    segs = 1
    for x in a:
        if x==curr_char:
            curr_len += 1
        else:
            segs += 1
            curr_len = 1
            curr_char = x
    return len(a)-max(1,segs-2*k)
n,k = map(int,input().split())
print(solve([1 if c=='L' else 0 for c in input()],k))