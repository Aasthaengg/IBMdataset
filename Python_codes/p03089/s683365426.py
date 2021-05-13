def main():
    N = int(input())
    B = list(map(int, input().split()))
    ans = list()
    while len(B) > 0:
        D = [(i + 1) - b for i, b in enumerate(B)]
        last_zero_index = -1
        for i, d in enumerate(D):
            if d < 0:
                print(-1)
                return
            if d == 0:
                last_zero_index = i
        if last_zero_index == -1:
            print(-1)
            return
        ans.append(B[last_zero_index])
        B = B[:last_zero_index] + B[(last_zero_index+1):]
    ans.reverse()
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()