from collections import defaultdict

memo = []


def find(nowstr, rest):
    if rest < 0:
        return ""

    for i in costlist:
        if i < rest:
            find(nowstr+str(i), rest - i)
        elif i == rest:

            memo.append(nowstr+str(i))


def cost_to_num(c):
    if c == 2:
        return "1"
    if c == 3:
        return "7"
    if c == 4:
        return "4"

    if c == 5:
        if 2 in num_to_use:
            return "2"
        elif 3 in num_to_use:
            return "3"
        else:
            return "5"
    if c == 6:
        if 6 in num_to_use:
            return "6"
        else:
            return "9"
    if c == 7:
        return "8"


N, M = map(int, input().split())
Alist = list(map(int, input().split()))

num_to_use = set(Alist)
"""
1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 を 1 つ作るには、
2 , 5 , 5 , 4 , 5 , 6 , 3 , 7 , 6 本のマッチ棒を使う。
"""
ref = [2, 5, 5, 4, 5, 6, 3, 7, 6]
if 9 in num_to_use:
    num_to_use.discard(6)
if 5 in num_to_use:
    num_to_use.discard(2)
    num_to_use.discard(3)
if 3 in num_to_use:
    num_to_use.discard(2)


costlist = [ref[i-1] for i in num_to_use]
costlist.sort()
# print(num_to_use)
# print(costlist)
# print(costlist[0])
minlength = N // costlist[0] - 5
if minlength < 0:
    minlength = 0
ans_tail = [cost_to_num(costlist[0])]*minlength

delta = N - minlength * costlist[0]
# print(delta)
find("", delta)

# print(memo)

ans_length = len(memo[0])
temp = 0
for i in memo:
    if len(i) < ans_length:
        continue

    numlist = [cost_to_num(int(j)) for j in i]+ans_tail
    # print(numlist)
    numlist.sort(reverse=True)
    joined = "".join(numlist)
    # print(joined)
    if temp < int(joined):
        temp = int(joined)
ans_head = str(temp)

# print("---")
print(ans_head)
