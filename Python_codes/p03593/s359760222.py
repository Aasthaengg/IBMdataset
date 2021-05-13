import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import Counter
def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.extend(list(input()))
    a_ac = Counter(a)
    a_ac_v = list(a_ac.values())
    a_ac_v.sort(reverse=True)
    if h == 1 or w == 1:
        a_ac_v_parity_ac = Counter([i & 1 for i in a_ac_v])
        if h&1 == 1 and w&1 == 1:
            if a_ac_v_parity_ac[1] == 1:
                print('Yes')
            else:
                print('No')
            sys.exit()
        else:
            if a_ac_v_parity_ac[1] >= 1:
                print('No')
            else:
                print('Yes')
            sys.exit()

    num = []
    num.extend([4] * ((h // 2) * (w // 2)))

    if h&1:
        num.extend([2] * (w // 2))
    if w&1:
        num.extend([2] * (h // 2))
    if h&1 and w&1:
        num.extend([1])
    while sum(num):
        if a_ac_v[0] >= num[0]:
            a_ac_v[0] -= num[0]
            num[0] = 0
            a_ac_v.sort(reverse=True)
            num.sort(reverse=True)
        else:
            break
    if num[0] == 0 and a_ac_v[0] == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()