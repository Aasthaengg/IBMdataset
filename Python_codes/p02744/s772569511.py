N = int(input())
ans = []


def get_range(s):
    start = ord("a")
    end = ord(max(s))
    return [chr(c) for c in range(start, end + 2)]


def pana(s):
    if len(s) == N:
        ans.append(s)
        return
    for t in get_range(s):
        pana(s + t)
    return


pana("a")
ans.sort()
print(*ans, sep="\n")