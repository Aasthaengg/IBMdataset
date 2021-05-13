S = input()
color = S[0]
cnt = 0
for i in S[1:]:
    if i != color:
        cnt += 1
        color = i
print(cnt)