abc = list(map(int, input().split()))
a, b, c = sorted(abc)
cou = c - b
if (b-a) % 2 == 0:
    cou += (b-a)//2
else:
    cou += (b-a)//2 + 2
print(cou)