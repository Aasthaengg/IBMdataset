S = input()
ABD = S.replace("BC","D")
a_cnt = 0
ans = 0
# print(ABD)
# print(S)
for s in ABD:
    if s == 'A':
        a_cnt += 1
    elif s == 'D':
        ans += a_cnt
    elif s == 'B' or s == 'C':
        a_cnt = 0
print(ans)