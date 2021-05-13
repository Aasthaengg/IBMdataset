S = input()
head, tail, ans = 0, len(S)-1, 0

while head < tail:
    if S[head] == S[tail]:
        head += 1
        tail -= 1
    elif S[head] == 'x':
        head += 1
        ans += 1
    elif S[tail] == 'x':
        tail -= 1
        ans += 1
    else:
        print(-1)
        exit()
print(ans)