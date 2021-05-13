h, w, k = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(map(int, list(input()))))

def vertical_line(h, w, k, s):
    ans = 0
    mark = [0 for _ in range(h)]
    for i in range(w):
        for j in range(h):
            mark[j] += s[j][i]
            if mark[j] > k:
                ans += 1
                mark = [s[l][i] for l in range(h)]
                break
    return ans

from copy import deepcopy
ans = []
for i in range(2 ** (h - 1)):
    s_copy = deepcopy(s)
    flag = False
    h_copy = h
    for j in range(h - 2, -1, -1):
        if i % 2 == 1:
            h_copy -= 1
            for l in range(w):
                s_copy[j][l] += s_copy[j+1][l]

                if s_copy[j][l] > k:
                    flag = True
                    break

            del s_copy[j+1]

        if flag:
            break

        i //= 2

    if flag:
        continue

    ans.append(h_copy - 1 + vertical_line(h_copy, w, k, s_copy))
print(min(ans))