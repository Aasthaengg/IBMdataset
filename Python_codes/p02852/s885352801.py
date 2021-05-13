from collections import Counter

mod = 1000000007


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft

s = ['SUN', 'MON','TUE','WED','THU','FRI','SAT']

def main():
    n, m = map(int, input().split())
    s = input()
    s = list(reversed(s))
    i = 0
    ans = []
    while i < n:
        next = i
        for j in range(i+1, min(i+m+1, n+1)):
            if s[j] == '0':
                next = j
        if next == i:
            print(-1)
            return
        ans.append(next-i)
        i = next
    print(' '.join(str(i) for i in reversed(ans)))
main()
