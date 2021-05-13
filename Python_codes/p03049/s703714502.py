N = int(input())
S = []

ans = 0
end_a = 0
start_b = 0
both = 0
for i in range(N):
    s = input()
    S.append(s)
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        both += 1
    elif s[-1] == 'A':
        end_a += 1
    elif s[0] == 'B':
        start_b += 1

if both == 0:
    ans += min(start_b, end_a)
else:
    if start_b == end_a == 0:
        ans += both - 1
    else:
        ans += both + min(start_b, end_a)

print(ans)
