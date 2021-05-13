N = int(input())
if N % 2:
    print(0)
    exit()
ans = 0
tmp = 10
while N >= tmp:
    ans += N//tmp
    tmp *= 10
tmp = 50
tmp_2 = 100
while N >= tmp:
    ans += N//tmp - N//tmp_2
    tmp *= 5
    tmp_2 *= 10
print(ans)
ans = 0