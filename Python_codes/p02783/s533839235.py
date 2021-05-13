h, a = map(int, input().split())
amari = h % a
shou = h // a
if amari == 0:
    print(shou)
else:
    print(shou +1)