def ask(q):
    print(q, flush=True)
    inp = input()
    if inp == "Vacant":
        exit()
    return inp


n = int(input())

l = ask(0)
r = ask(n-1)
left = 0
right = n-1

for _ in range(18):
    mid = (right + left) // 2
    m = ask(mid)

    if l == m and (mid - left) % 2 == 1:
        right = mid
        r = m
    elif l != m and (mid - left) % 2 == 0:
        right = mid
        r = m
    else:
        left = mid
        l = m
