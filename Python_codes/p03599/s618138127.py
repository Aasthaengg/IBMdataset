# まずは全探索砂糖の質量、水の質量はともにO(F^2)だがそれらの組み合わせもO(F^2)であること（上限がFだから）に注意
A,B,C,D,E,F = map(int,input().split())
water = set()
for water1 in range(0,F+1,100*A):
    for water2 in range(0,F+1,100*B):
        if water1 + water2 <= F:
            water.add(water1+water2)

sugar = set()
for sugar1 in range(0,F+1,C):
    for sugar2 in range(0,F+1,D):
        if sugar1 + sugar2 <= F:
            sugar.add(sugar1+sugar2)
# print(water)
# print(sugar)
ans_s = 0
ans_w = 0
max_c = 0
for w in water:
    for s in sugar:
        if 0< w + s <= F:
            if w//100*E >= s:
                if max_c < (100*s)/(s+w):
                    ans_s = s
                    ans_w = w
                    max_c = (100*s)/(s+w)

if ans_s == 0 and ans_w == 0:
    ans_w = 100*A
print(ans_w+ans_s,ans_s)
