N = int(input())
Bs = list(map(int, input().split()))
ans = []


def solve(acc, xs):
    head, *tail = xs
    if not acc:
        acc.append(head)
    if not tail:
        acc.append(head)
        return acc

    peek, *_ = tail
    acc.append(min(head, peek))
    return solve(acc, tail)


arr = solve([], Bs)
print(sum(arr))
