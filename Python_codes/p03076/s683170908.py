import itertools

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num_list = [a, b, c, d, e]
factorial = list(itertools.permutations(num_list, 5))
ans_list = []
for list in factorial:
    tmp = 0
    for i in list:
        if tmp%10 == 0:
            tmp += i
        else:
            tmp += 10 - tmp%10
            tmp += i
    ans_list.append(tmp)

ans_list.sort()
ans = ans_list[0]

print(ans)