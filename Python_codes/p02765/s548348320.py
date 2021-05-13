def solve():
    if n>=10:
        return r
    else:
        return r+100*(10-n)


n, r = [int(i) for i in input().split(" ")]
print(solve())