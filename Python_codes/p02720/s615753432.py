def incr_lunlun(num):
    num[0] += 1
    if len(num) == 1:
        if num[0] == 10:
            num.append(1)
            num[0] = 0
    
    elif num[0] > num[1] + 1 or num[0] == 10:
        suffix = incr_lunlun(num[1:])
        digit = max(0, suffix[0] - 1)
        num = [digit] + list(suffix)

    return num


def main():
    k = int(input())
    num = [1]
    for i in range(k-1): 
        num = incr_lunlun(num)

    print(int(''.join(str(i) for i in reversed(num))))



main()
