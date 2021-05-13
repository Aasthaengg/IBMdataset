def main():
    S = [s for s in input()]
    num_a = num_b = num_c = 0
    for s in S:
        if s == 'a':
            num_a += 1
        elif s == 'b':
            num_b += 1
        elif s == 'c':
            num_c += 1
    num = [num_a, num_b, num_c]
    num.sort(reverse=True)
    for i in range(len(S)):
        index = i % 3
        if num[index] == 0:
            print('NO')
            return
        num[index] -= 1
    print('YES')
    return

if __name__ == '__main__':
    main()
