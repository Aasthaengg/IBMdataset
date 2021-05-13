from bisect import bisect_left, insort_left

S = list(input())

alpha = [chr(i) for i in range(ord("a"), ord("a") + 26)]

not_used = list(set(alpha) - set(S))
not_used.sort()

if not not_used:
    can = []
    flag = True
    for i in range(len(S)-1, -1 , -1):
        idx = bisect_left(can, S[i])
        if idx == len(can):
            insort_left(can, S[i])
        else:
            S[i] = can[idx]
            idx = i
            flag = False
            break
    if flag:
        print(-1)
    else:
        print(*S[:idx+1], sep="")
else:
    S.append(not_used[0])
    print(*S, sep="")