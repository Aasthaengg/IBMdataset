n = int(input())
s = []
last_a = 0
first_b = 0
cnt = 0
both = 0
for i in range(n):
    ss = input()
    s.append(ss)
    if ss[0] == 'B':
        first_b += 1
    if ss[-1] == 'A':
        last_a += 1
    if ss[0] == 'B' and ss[-1] == 'A':
        both += 1
        last_a -= 1
        first_b -= 1

    for j in range(len(ss)-1):
        if ss[j] == 'A' and ss[j+1] == 'B':
            cnt += 1

sub = abs(first_b - last_a)
sub2 = both - sub
ans = cnt
if both == 0:
    ans += min(first_b,last_a)
elif first_b == last_a == 0:
    ans += max(0,both - 1)
else:
    ans += min(first_b,last_a) + min(sub,both) + max(0,sub2)

print(ans)
