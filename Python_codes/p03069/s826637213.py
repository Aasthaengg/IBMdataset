def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    s = input()
    a, b = [0], [0]
    for i in range(N):
        if s[i] == '#': a.append(a[-1]+1)
        else: a.append(a[-1])

        if s[-1-i] == '.': b.append(b[-1]+1)
        else: b.append(b[-1])
    b = b[::-1]
    output =  10 ** 6
    for x, y in zip(a, b): output = min(output, x + y)
    print(output)

    return

if __name__ == '__main__':
    main()
