def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    X = ii()
    l = []
    for b in range(1, 1001):
        if b == 1:
            l.append(1)
            continue
        a = b*b
        while a <= X:
            l.append(a)
            a *= b
    print(max(l))

if __name__ == '__main__':
    main()