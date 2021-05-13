S = input()
L = [0] * len(S)
now = 0
RorL_count = 0
for i in range(len(S)):
    if (i == len(S) - 1 and S[now] == 'R'):
        if ((i - now) % 2 == 0):
            L[i] += (RorL_count // 2)
            L[i - 1] += (RorL_count // 2)
        else:
            L[i - 1] += (RorL_count // 2 + 1)
            L[i] += (RorL_count // 2)
        L[i] += 1
        break
    elif (i == len(S) - 1 and S[now] == 'L'):
        RorL_count += 1
        if ((i - now) % 2 == 0):
            L[now] += (RorL_count // 2 + 1)
            L[now - 1] += (RorL_count // 2)
        else:
            L[now] += (RorL_count // 2)
            L[now - 1] += (RorL_count // 2)
        break

    if (S[now] == 'R'):
        if (S[i] == 'L'):
            if ((i - now) % 2 == 0):
                L[i] += (RorL_count // 2)
                L[i - 1] += (RorL_count // 2)
            else:
                L[i - 1] += (RorL_count // 2 + 1)
                L[i] += (RorL_count // 2)
            RorL_count = 1
            now = i
        else:
            RorL_count += 1
            continue
    else:
        if (S[i] == 'R'):
            if ((i - now) % 2 == 0):
                L[now] += (RorL_count // 2)
                L[now - 1] += (RorL_count // 2)
            else:
                L[now] += (RorL_count // 2 + 1)
                L[now - 1] += (RorL_count // 2)
            RorL_count = 1
            now = i
        else:
            RorL_count += 1
            continue
strL = []
for i in L:
    strL.append(str(i))
print(' '.join(strL))
