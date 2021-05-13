def main():
    n = int(input())
    m = 100 // 7 + 1
    flag = False
    for i in range(m):
        for j in range(m):
            if n == i * 7 + j * 4:
                flag = True
                if flag:
                    print('Yes')
                    break
        else:
            continue
        break
    if not flag:
        print('No')
if __name__ == '__main__':
    main()