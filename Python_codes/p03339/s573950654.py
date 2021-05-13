input()
S = input()

ans = ans_cur = S.count("E")
for c in S:
    if c == "E":
        ans_cur -= 1
    else:
        ans_cur += 1
    ans = ans if ans <= ans_cur else ans_cur
print(ans)