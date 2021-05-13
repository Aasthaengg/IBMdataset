num_in = [int(i) for i in input().split()]

def calc_dig_sum(num):
    num_str = str(num)
    ret = 0
    for c in num_str:
        ret += int(c)
    return ret

sum = 0
for i in range(1, num_in[0]+1):
    if num_in[1] <= calc_dig_sum(i) <= num_in[2]:
        sum += i

print(sum)