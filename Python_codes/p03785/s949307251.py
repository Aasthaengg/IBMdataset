n,c,k = map(int, input().split())
t = sorted(list(int(input()) for _ in range(n)))

#Ti以上Ti+k以下のバスに乗る
#定員はC人

T = 0
cnt = 0
bus = 0
for i in range(n):
    if cnt == 0:
        cnt += 1
        T = t[i] + k
    elif T >= t[i]:
        cnt += 1
    elif T < t[i]:
        bus += 1
        cnt = 1
        T = t[i]+k
    if cnt == c:
        bus += 1
        T = 0
        cnt = 0
if cnt != 0: bus += 1
print(bus)