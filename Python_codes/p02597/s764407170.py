n = int(input())
c = input()

wr = c.count('WR')
r = c.count('R')
w = c.count('W')

if wr == 0:
    print(0)
else:
    c_sorted = 'R'*r + 'W'*w
    ans = 0
    for i in range(n):
        if c[i] != c_sorted[i]:
            ans += 1
        else:
            ans += 0
    print(ans//2)