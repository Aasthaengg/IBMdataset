n = int(input())
ans = []
now = n
cou = 1
if n == 0:
    print(0)
    exit()
while True:
    if now == 0:
        break
    if now % (2**cou) == 2**(cou-1):
        ans.append(1)
        now -= (-2)**(cou-1)
    elif now % (2**cou) == 0:
        ans.append(0)
    cou += 1

for i in reversed(range(len(ans))):
    print(ans[i],end="")
print()