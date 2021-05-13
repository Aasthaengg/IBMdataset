import bisect
import sys
input = sys.stdin.readline

def main():
    a,b,q = map(int,input().split())
    s = []
    t = []
    s1 = []
    t1 = []

    for _ in range(a):
        s.append(int(input()))
    for _ in range(b):
        t.append(int(input()))

    for i in range(a-1):
        s1.append((s[i]+s[i+1])/2)
    for i in range(b-1):
        t1.append((t[i]+t[i+1])/2)

    for _ in range(q):
        x = int(input())
        s_index = bisect.bisect_left(s1, x)
        t_index = bisect.bisect_left(t1, x)
        xs = []
        xt = []
        for i in range(-2, 3):
            if 0 <= s_index + i < a:
                xs.append(s[s_index+i])
            if 0 <= t_index + i < b:
                xt.append(t[t_index+i])
        ans = 10**20
        for i in xs:
            for j in xt:
                ans = min(ans, abs(x-i) + abs(i-j), abs(x-j) + abs(j-i))

        print(ans)

if __name__ == '__main__':
    main()