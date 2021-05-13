def main():
    n = int(input())

    count_list = [0] * n
    upper = int(n**0.5) + 2
    for x in range(1, upper):
        for y in range(1, upper):
            for z in range(1, upper):
                num = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if num <= n:
                    count_list[num-1] += 1
    for count in count_list:
        print(count)


if __name__ == '__main__':
    main()
