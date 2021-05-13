from bisect import bisect_left

N = int(input())

cum = [0]
now = 1

while cum[-1] <= N:
    cum.append(now + cum[-1])
    now += 1

# print(len(cum))
# cum[i]; cum[i]までの数はiまでの和で表せる
idx = bisect_left(cum, N)
# print(cum, idx)
# idxまでの数の中から選んで和をNにする
ans = []
tmp = 0
i = idx
while i > 0:
    # print(i, tmp)
    tmp += i
    ans.append(i)
    if tmp == N:
        print(*ans)
        exit()
    elif tmp > N:
        tmp -= i
        i -= 1
        ans.pop()
    else:
        i -= 1
