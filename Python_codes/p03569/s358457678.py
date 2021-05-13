s = input()
S = []
for i in range(len(s)):
    S.append(s[i])

check = []
for i in S:
    if i == 'x':
        continue
    else:
        check.append(i)

if check == check[::-1]:
    # 先頭の文字と最後の文字が一致しているかを調べ一致していれば、除く、一致していなければ、xを加える
    first = 0
    last = len(S) - 1
    count = 0
    while first < last:
        if S[first] != S[last] and S[first] == 'x':
            count += 1
            first += 1
            continue
        elif S[first] != S[last] and S[last] == 'x':
            count += 1
            last -= 1
            continue
        else:
            first += 1
            last -= 1
            continue
    print(count)

else:
    print(-1)
