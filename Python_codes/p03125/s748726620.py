#約数列挙
def make_divisor_list(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = []
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        divisor_list.append(num)

        return divisor_list

def main():
    A,B = map(int, input().split())
    div_list = make_divisor_list(B)

    if A in div_list:
        print(A+B)
    else:
        print(B-A)


if __name__ == '__main__' :
    main()