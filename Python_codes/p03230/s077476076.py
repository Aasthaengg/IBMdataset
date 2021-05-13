n = int(input())

i = 1
cnt = 1
flag = False
while True:
    cnt += 1
    if i == n:
        flag = True
        break
    if i > n:
        break
    i += cnt

# nがkC2(kは自然数) <-> 構築可能
if not flag:
    print("No")
    exit()

print("Yes")
print(cnt)
li = [[] for i in range(cnt)]
num = 1
for i in range(cnt):
    tmp_num = num
    for _ in range(cnt - i - 1):
        li[i].append(tmp_num)
        tmp_num += 1
    for j in range(i+1, cnt):
        li[j].append(num)
        num += 1
for li2 in li:
    print(len(li2), *li2)