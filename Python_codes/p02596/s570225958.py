# Ai ≡ 0 (mod k) A1 = 7, A2 = 77, A3 = 777

k = int(input())
if k == 7 or k == 1:
    print(1)
    exit()
# よくわからんからAiをmodKにして試してみる
seven = 7
for i in range(1, 10**6 + 10):
    seven = seven * 10 + 7
    seven %= k
    if seven == 0:
        print(i + 1)
        exit()
print(-1)