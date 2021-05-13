import sys
import bisect
def main():
    input = sys.stdin.readline
    s = input().rstrip()
    t = input().rstrip()

    letters = set(t)
    indices = dict()
    for l in letters:
        lst = []
        left = 0
        while left < len(s):
            i = s.find(l, left)
            if i < 0: break
            lst.append(i)
            left = i+1
        if not lst:
            print(-1)
            exit()
        indices[l] = lst
    
    offset = 0
    cycle = 0
    for l in t:
        ind = indices[l]
        i = bisect.bisect_left(ind, offset)
        if i < len(ind):
            offset = ind[i] + 1
        else:
            offset = ind[0] + 1
            cycle += 1
        if offset >= len(s):
            offset %= len(s)
            cycle += 1

    print(len(s)*cycle + offset)

if __name__ == '__main__':
    main()