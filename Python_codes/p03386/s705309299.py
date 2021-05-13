def main():
    a, b, k = map(int, input().split())
    printed = 0
    l = []
    for i in range(k):
        if a + i > b:
            return
        print(a + i)
        printed = a + i
        l.append(printed)
    if printed >= b:
        return
    for i in range(k):
        if b - k + 1 + i in l:
            continue
        elif b - k + 1 + i > b:
            break
        print(b - k + 1 + i)

main()