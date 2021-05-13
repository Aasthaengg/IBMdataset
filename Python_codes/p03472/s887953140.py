n, h = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(n)]
A,B = zip(*AB)
a = max(A)
B = [b for b in B if b > a]
B.sort(reverse=True)
ans = 0
hp = h
attack_cnt = 0
for b in B:
    if hp <= 0:
        break
    attack_cnt += 1
    hp -= b
if hp > 0:
    attack_cnt += (hp - 1) // a + 1
print(attack_cnt)
