n = int(input())
ab, tail_a, head_b, th_a = 0, 0, 0, 0

for _ in range(n):
    s = input()
    ab += s.count('AB')
    if s[-1] == 'A' and s[0] == 'B': th_a += 1
    elif s[-1] == 'A': tail_a += 1
    elif s[0] == 'B': head_b += 1

if tail_a+head_b == 0 and th_a > 0:
    print(ab + th_a - 1)
else:
    if min(tail_a, head_b) + th_a == n:
        print(ab + min(tail_a, head_b) + th_a - 1)
    else:
        print(ab + min(tail_a, head_b) + th_a)
