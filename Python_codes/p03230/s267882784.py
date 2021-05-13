from itertools import combinations as comb


def comb2(a):
    return a * (a - 1) // 2


n = int(input())

numS = 2
while True:
    if n < comb2(numS):
        print("No")
        exit()
    elif n == comb2(numS):
        break
    numS += 1

lenS = n * 2 // numS

print("Yes")
print(numS)
ans = {}
for i, room in enumerate(comb(range(numS), 2)):
    # print(room)
    for a in room:
        if a not in ans:
            ans[a] = [str(i + 1)]
        else:
            ans[a].append(str(i + 1))


for ansS in ans.values():
    print(str(lenS) + " " + " ".join(ansS))