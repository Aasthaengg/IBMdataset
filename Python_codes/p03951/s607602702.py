#!/usr/bin/env python3

N = int(input())
S = input()
T = input()


ans = S + T
end = N
for i in range(N):
    if S[i:] == T[:end]:
        ans = S + T[end:]
        break

    end -= 1

print(len(ans))
