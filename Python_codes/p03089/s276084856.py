import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    b = in_nl()

    ans = []
    while True:
        ind = -1
        for i in range(len(b)):
            if i+1 == b[i]:
                ind = i
        if ind != -1:
            b.pop(ind)
            ans.append(ind+1)
            if len(b) == 0:
                break
        else:
            break

    if len(b) == 0:    
        print('\n'.join(map(str, (ans[::-1]))))
    else:
        print(-1)





if __name__ == '__main__':
    main()
