s = input()
# ABC -> BCA
# "BC"を纏めて考える
s = s.replace('BC', 'D')
# AとDだけからなる部分列において、各Dについて、左にあるAの数を数える
# 部分列は最終的に D...DA...Aとなる
ans = 0
cntA = 0
for i in range(len(s)):
    if s[i] == 'A':
        cntA += 1
    elif s[i] == 'D':
        ans += cntA
    # AとD以外(= B or C)の場合は一旦途切れる
    else:
        cntA = 0

print(ans)
