n = int(input())
s = list(input())
white = 0
black = 0
for i in range(n):
    if s[i] == '.':
        white+=1

ans = white
for i in range(n):
    if s[i] == '.':
        white -= 1
    else:
        black += 1
    ans = min(ans, white + black)
print(ans)

