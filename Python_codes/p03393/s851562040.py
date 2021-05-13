def main():
    S = input()
    N = len(S)
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for d in dic:
        if d in S:
            continue
        else:
            return print(S + d)
    if S == "zyxwvutsrqponmlkjihgfedcba":
        return print(-1)
    pre = S[-1]
    used = [S[-1]]
    from heapq import heapify, heappop, heappush
    heapify(used)
    for i in range(N-1)[::-1]:
        if S[i] < pre:
            c = heappop(used)
            while S[i] > c:
                c = heappop(used)
            print(S[:i] + c)
            break
        else:
            pre = S[i]
            heappush(used, pre)


if __name__ == '__main__':
    main()
