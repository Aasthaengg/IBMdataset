S = list(input())

ans = [0]
ans_ = 0
for s in S:
    if s == "A" or s == "C" or s == "G" or s == "T":
        ans_ += 1
    else:
        ans.append(ans_)
        ans_ = 0
ans.append(ans_)
print(max(ans))
