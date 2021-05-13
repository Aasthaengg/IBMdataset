import collections
import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    S = [input() for _ in range(n)]
    word = collections.Counter(S).most_common()
    maxi = word[0][1]
    ans = []
    for w in word:
        if w[1] == maxi:
            ans.append(w[0])
        else:
            break
    ans.sort()
    a = "\n".join(ans)
    print(a)

if __name__ == '__main__':
    main()