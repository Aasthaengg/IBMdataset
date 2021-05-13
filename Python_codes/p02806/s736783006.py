if __name__ == '__main__':
    n = int(input())
    list =[]
    sumN=0
    for i in range(n):
        a = [str(i) for i in input().split()]
        list.append(a)
        sumN += int(a[1])
    x = input()

    for i in list:
        sumN -= int(i[1])
        if x == i[0]:
            break
    print(sumN)
