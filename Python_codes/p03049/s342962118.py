N = int(input())

ans = 0
ab = 0
tail_a = 0
head_b = 0

for _ in range(N):
    s = input()
    ans += s.count('AB')

    if s[-1] == 'A' and s[0] == 'B':
        ab += 1
    elif s[-1] == 'A' and s[0] != 'B':
        tail_a += 1
    elif s[-1] != 'A' and s[0] == 'B':
        head_b += 1

if ab == 0:
    print(ans+min(tail_a, head_b))
elif ab > 0 and max(tail_a, head_b) > 0:
    print(ans+ab+min(tail_a, head_b))
elif max(tail_a, head_b) == 0:
    print(ans+ab-1)
