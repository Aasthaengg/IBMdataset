def main():
    n = int(input())
    p = [True] * 55556
    p[0] = False
    p[1] = False
    curr = 2
    while curr * curr <= 55555:
        if p[curr]:
            for i in range(curr * curr, 55556, curr):
                p[i] = False
        curr += 1
    fives = []
    for i in range(2, 55556):
        if p[i] and i % 5 == 1:
            fives.append(i)
    print(*fives[:n])
    

if __name__ == '__main__':
    main()