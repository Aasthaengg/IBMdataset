def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    a = [0]+list(mi())
    b = [0]*(N+1)
    for i in range(N, 0, -1):
        if i > N//2:
            b[i] = a[i]
        else:
            b[i] = (a[i]+sum(b[i*2::i]))%2
    print(sum(b))
    print(' '.join([str(i) for i in range(N+1) if b[i]]))

if __name__ == '__main__':
    main()