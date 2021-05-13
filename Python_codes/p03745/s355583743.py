n = int(input())
a_l = list(map(int, input().split()))
ans = 1
is_plus = None
sub = []
for i in a_l:
    if len(sub) == 0:
        sub.append(i)
        continue
    if i == sub[-1]:
        sub.append(i)
        continue

    if is_plus is None:
        if sub[-1] > i:
            is_plus = False
        else:
            is_plus = True
        sub.append(i)

    elif is_plus is True:
        if sub[-1] > i:
            sub = [i]
            ans += 1
            is_plus = None
        else:
            sub.append(i)
    else:
        if sub[-1] < i:
            sub = [i]
            ans += 1
            is_plus = None
        else:
            sub.append(i)
print(ans) 