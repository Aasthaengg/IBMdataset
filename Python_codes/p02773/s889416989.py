import sys
import collections

input = sys.stdin.readline

def main():
    N = int(input())
    Slist = []
    for _ in range(N):
        Slist.append(str(input()[:-1]))
    SlistCounter = list(collections.Counter(Slist).items())
    SlistCounter.sort(key=lambda x: x[0])
    SlistCounter.sort(key=lambda x: x[1], reverse=True)
    maxcnt = SlistCounter[0][1]
    for s, cnt in SlistCounter:
        if cnt != maxcnt:
            break
        print(s)

if __name__ == "__main__":
    main()
