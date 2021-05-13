n = int(input())
s = input()
bag = []
cnt = 0
for i in s:
    if i == "I":
        cnt += 1
        bag.append(cnt)
    else:
        cnt -= 1
        bag.append(cnt)
ans = max(bag)
if ans < 0:
    print(0)
else:
    print(ans)