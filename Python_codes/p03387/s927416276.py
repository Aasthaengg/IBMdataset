def main():
    abc = list(map(int, input().split()))

    abc_sort = sorted(abc)
    min_num, mid_num, max_num = abc_sort
    Count = 0
    while(max_num - min_num > 1):
        diff = max_num - min_num
        Count += diff//2
        abc_sort[0] += (diff//2) * 2
        abc_sort = sorted(abc_sort)
        max_num = abc_sort[2]
        min_num = abc_sort[0]

    if (abc_sort[2] - abc_sort[1] == 1):
        Count += 1
    elif (abc_sort[2]-abc_sort[1] == 0 and abc_sort[1] - abc_sort[0] == 1):
        Count += 2
    print(Count)


if __name__ == "__main__":
    main()
