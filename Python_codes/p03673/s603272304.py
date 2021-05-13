# C - pushpush
def main():
    from collections import deque
    n = int(input())
    a = list(map(int, input().split()))
    ans = deque(maxlen=2*10**5)

    for i in range(n):
        if n % 2 == 0:
            if i % 2 == 0:
                ans.append(str(a[i]))
            else:
                ans.appendleft(str(a[i]))
        else:
            if i % 2 == 0:
                ans.appendleft(str(a[i]))
            else:
                ans.append(str(a[i]))

    else:
        print(' '.join(ans))


if __name__ ==  "__main__":
    main()