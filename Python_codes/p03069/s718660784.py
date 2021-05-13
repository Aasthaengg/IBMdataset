N = int(input())
S = input()

right_white = S.count(".")
left_black = 0

ans = right_white + left_black
for i in range(N):
    if S[i] == ".":
        right_white -= 1
    else:
        left_black += 1
    ans = min(ans, right_white + left_black)

print(ans)