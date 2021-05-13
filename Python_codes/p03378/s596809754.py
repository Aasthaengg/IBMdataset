def main():
    l = [int(_) for _ in input().split()]
    n = l[0]
    m = l[1]
    x = l[2]
    a = [int(_) for _ in input().split()]

    cost_to_zero = 0
    cost_to_m = 0

    for i in range(len(a)):
        if a[i] > x:
            cost_to_m += 1
        else:
            cost_to_zero += 1

    answer = min([cost_to_zero, cost_to_m])
    print(answer)


if __name__ == "__main__":
    main()
