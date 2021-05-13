import itertools

def main(L):
    ans = 0
    for pair in itertools.combinations(L, 3):
        if len(set(pair)) < 3:
            continue
        lines = list(pair)
        a = max(lines)
        lines.remove(a)
        b, c = lines
        if a < b + c:
            ans += 1
    return ans

if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    ans = main(L)
    print(ans)

