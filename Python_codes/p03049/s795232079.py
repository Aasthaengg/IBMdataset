n = int(input())
naibu = 0
head = 0
tail = 0
both = 0

for _ in range(n):
    s = str(input())
    naibu += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        both += 1
    elif s[0] == 'B':
        head += 1
    elif s[-1] == 'A':
        tail += 1

ans = min(head, tail) + both + naibu
if head == 0 and tail == 0:
    ans = max(both-1, 0) + naibu
print(ans)