n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

if sum(a_list) < sum(b_list):
    print(-1)
    exit()

a_sub_b = [a_list[i] - b_list[i] for i in range(n)]
insufficients = [x for x in a_sub_b if x < 0]

cnt = len(insufficients)
sum_insuf = sum(insufficients)
for x in sorted(a_sub_b, reverse=True):
    if sum_insuf >= 0:
        break
    sum_insuf += x
    cnt += 1
print(cnt)
