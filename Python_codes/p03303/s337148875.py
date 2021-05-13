# B - Acrostic
# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_b

# 指定した文字数ずつ分割　chunk

S = input()
w = int(input())

sp = [S[i: i+w] for i in range(0, len(S), w)]

ans = "".join(s[0] for s in sp)

print(ans)
