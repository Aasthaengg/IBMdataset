import sys
import re
import heapq

def value(t):
    global a, b, c
    return -(a[t[0]] + b[t[1]] + c[t[2]])

def main():
    global a, b, c
    x, y, z, k = map(int, re.split(r'\s+', sys.stdin.readline().strip()))
    #print(x, y, z, k)
    a = list(map(int, re.split(r'\s+', sys.stdin.readline().strip())))
    b = list(map(int, re.split(r'\s+', sys.stdin.readline().strip())))
    c = list(map(int, re.split(r'\s+', sys.stdin.readline().strip())))

    a.sort()
    b.sort()
    c.sort()

    done = set()
    q = list()
    t = (x - 1, y - 1, z - 1)
    q.append((value(t), t))

    for _ in range(k):
        val, t = heapq.heappop(q)
        print(-val)
        t0 = (t[0] - 1, t[1], t[2])
        t1 = (t[0], t[1] - 1, t[2])
        t2 = (t[0], t[1], t[2] - 1)
        if (t0 not in done) and (t[0] - 1 >= 0):
            heapq.heappush(q, (value(t0), t0))
            done.add(t0)
        if (t1 not in done) and (t[1] - 1 >= 0):
            heapq.heappush(q, (value(t1), t1))
            done.add(t1)
        if (t2 not in done) and (t[2] - 1 >= 0):
            heapq.heappush(q, (value(t2), t2))
            done.add(t2)
            
main()
