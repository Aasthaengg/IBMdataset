import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
s = input().rstrip()
s_rev = s[::-1]

place = 0

ans = []

while place < n:
    flag = 1
    for i in range(min(m, n - place), 0, -1):
        if s_rev[place + i] == "0":
            ans.append(i)
            place += i
            flag = 0
            break
    if flag:
        print(-1)
        sys.exit()

print(*ans[::-1])
