N = int(input())
S = [input() for _ in range(N)]

cnt = 0
end_a = 0
sta_b = 0
a_b = 0
for s in S:
    cnt += s.count('AB')
    if s[-1]=='A' and s[0]=='B':
        a_b += 1
    elif s[-1]=='A':
        end_a += 1
    elif s[0]=='B':
        sta_b += 1
if a_b>=1:
    cnt += a_b-1
    if end_a>=1:
        end_a -= 1
        cnt += 1
    if sta_b>=1:
        sta_b -=1
        cnt+=1
cnt += min(end_a, sta_b)

print(cnt)