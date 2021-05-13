def main():
    n, m = list(map(int, input().split()))
    dcon = [set() for _ in range(n)]
    for _ in range(m):
        s, c = tuple(map(int, input().split()))
        dcon[s-1].add(c)

    if any(len(d) > 1 for d in dcon):
        print(-1)
        return
    
    digits = [0] if n == 1 else [1] + [0] * (n-1)
    for i in range(n):
        if dcon[i]:
            digits[i] = dcon[i].pop()

    if digits[0] == 0 and n != 1:
        print(-1)

    else:
        print(''.join(map(str, digits)))

main()
