n = int(input())
check = 0
keep = []

def q(n, check):
    if n in keep:
        return check
    else:
        keep.append(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return q(n, check+1)
print(q(n,check)+1)
