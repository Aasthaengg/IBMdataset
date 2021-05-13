import math
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    tot = sum(A)

    cand = helper(tot)
    for i in cand:
        rems = []
        for j in range(N):
            r = A[j] % i
            if r > 0:
                rems.append(r)
        rems.sort()

        tot = sum(rems)
        prefixneg = [0]
        for j in range(len(rems)):
            prefixneg.append(prefixneg[-1] + rems[j])

        for j in range(len(rems)+1):
            pos = (len(rems)-j)*i - (tot - prefixneg[j])
            neg = prefixneg[j]
            if max(pos, neg) <= K:
                return i

    return 1


def helper(n):
    div = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
    return sorted(list(div), reverse = True)

if __name__ == '__main__':
    print(main())