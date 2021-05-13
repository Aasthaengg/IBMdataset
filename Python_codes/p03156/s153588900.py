N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

q_a = []
q_b = []
q_c = []

for p in P:
    if p <= A:
        q_a.append(p)
    elif p <= B:
        q_b.append(p)
    else:
        q_c.append(p)

ans = 0
while q_a:
    q_a.pop()
    if q_b:
        q_b.pop()
    else:
        break
    if q_c:
        q_c.pop()
    else:
        break
    ans += 1
print(ans)
