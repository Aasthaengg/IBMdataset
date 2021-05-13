# ペンキの種類を求めよ

abc = input()

ls_abc = abc.split()
len_abc = len(ls_abc)

for i in range(len_abc):
    ls_abc[i] = int(ls_abc[i])

# print(ls_abc)

counter = {}
# この状態では，カウンターがからッぽ．０にするためには１８．１９行目
for i in range(len_abc):
    x = ls_abc[i]

    if not x in counter:
        counter[x] = 0

    counter[x] = counter[x] + 1

print(len(counter))