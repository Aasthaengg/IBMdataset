# -*- coding: utf-8 -*-
S = input()
ans = 0
left, right = 0, len(S)-1
while left < right:
    if S[left] == S[right]:
        left += 1
        right -= 1
    elif S[left] == 'x':
        left += 1
        ans += 1
    elif S[right] == 'x':
        right -= 1
        ans += 1
    else:
        print(-1)
        exit()

print(ans)
