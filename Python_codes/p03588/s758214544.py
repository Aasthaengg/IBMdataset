n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

s.sort()

#print(s)

ans = (s[0][0] - 1) + (s[-1][0] - s[0][0] + 1) + (s[-1][1])

print(ans)