ls1 = input()
ls2 = input()

num = len(ls1)

ans = 0

for i in range(num):
    if ls1[i] != ls2[i]:
        ans += 1

print(ans)