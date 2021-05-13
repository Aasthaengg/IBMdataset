#!/usr/bin/env python3

S = input()
r_count = 0
l_count = 0
Ret = [1 for _ in range(len(S))]
b = -1
i = 0
while i < len(S):
    if i < len(S)-1 and S[i:i+2] == 'RL':
        if r_count % 2 == 0:
            Ret[i] += r_count//2
            Ret[i+1] += r_count//2
        else:
            Ret[i] += r_count//2
            Ret[i+1] += r_count//2 + 1

        if b != -1:
            if l_count % 2 == 0:
                Ret[b] += l_count//2
                Ret[b+1] += l_count//2
            else:
                Ret[b] += l_count//2 + 1
                Ret[b+1] += l_count//2
        b = i
        r_count = 0
        l_count = 0
        i += 1
    elif S[i] == 'R':
        Ret[i] = 0
        r_count += 1
    elif S[i] == 'L':
        Ret[i] = 0
        l_count += 1

    i += 1

if l_count % 2 == 0:
    Ret[b] += l_count//2
    Ret[b+1] += l_count//2
else:
    Ret[b] += l_count//2 + 1
    Ret[b+1] += l_count//2

print(*Ret)
