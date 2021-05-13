import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    n, m = LI()
    a = LI()
    b = [0 for _ in range(m)]
    c = [0 for _ in range(m)]

    for i in range(m):
        b[i], c[i] = LI()

    dic = collections.Counter(a)
    queue = collections.deque(sorted(list(set(a)|set(c))))

    mn = min(a)
    while queue[0] < mn:
        queue.popleft()

    for i in range(m):
        cnt = 0
        for x in queue:
            if x < c[i]:
                tem = dic[x]
                dic[x] = max(dic[x]-b[i], 0)
                b[i] -= tem-dic[x]
                dic[c[i]] += tem-dic[x]
                if dic[x] == 0:
                    cnt += 1
                if b[i] == 0:
                    break
            else:
                break
        for _ in range(cnt):
            queue.popleft()
    ans = 0
    for k, v in dic.items():
        ans += k*v

    print(ans)

        


main()
