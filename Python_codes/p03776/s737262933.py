
from math import factorial
# 組み合わせ
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


def main():
    num, min_num, max_num = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort(reverse=True)

    last_ind = 0
    for i in range(num):
        if data[0] == data[i]:
            last_ind = i
        else:
            break

    sum_now = sum(data[:min_num])
    avg = sum_now / min_num
    now_ind = min_num
    ans_count = 0

    while 1:
        if now_ind >= num:
            break
        if data[now_ind] < avg:
            break
        sum_now += data[now_ind]
        now_ind += 1
        avg = sum_now / now_ind

    in_count = 0
    for i in range(now_ind):
        if data[now_ind - 1] == data[i]:
            in_count += 1

    out_count = 0
    for i in range(now_ind, num):
        if data[now_ind - 1] == data[i]:
            out_count += 1

    # print(in_count, out_count)

    if now_ind - 1 <= last_ind:
        toori = 0
        for i in range(min_num, min(now_ind + 1, max_num + 1)):
            toori += combinations_count(last_ind + 1, i)
    else:
        toori = combinations_count(in_count + out_count, in_count)

    # print(in_count, out_count, last_ind, now_ind)

    print(avg)
    print(toori)





if __name__ == '__main__':
    main()