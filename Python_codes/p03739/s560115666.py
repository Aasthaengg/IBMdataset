def first_positive(n,a):
    count = 0
    sum = a[0]
    #正ならTrue
    flag = True

    if a[0] <= 0:
        sum = 1
        count += abs(1 - a[0])

    for i in range(1,n):
        if sum + a[i] < 0 and flag == True:
            sum += a[i]
            flag = False
            continue
        elif sum + a[i] <= 0 and flag == False:
            flag = True
            count += abs(1 - sum - a[i])
            sum = 1
        elif sum + a[i] >= 0 and flag == True:
            flag = False
            count += abs(-1 - sum - a[i])
            sum = -1
        elif sum + a[i] > 0 and flag == False:
            sum += a[i]
            flag = True
            continue

    return count

def first_negative(n,a):
    count = 0
    sum = a[0]
    #正ならTrue
    flag = False

    if a[0] >= 0:
        sum = -1
        count += abs(-1 - a[0])

    for i in range(1,n):
        if sum + a[i] < 0 and flag == True:
            sum += a[i]
            flag = False
            continue
        elif sum + a[i] <= 0 and flag == False:
            flag = True
            count += abs(1 - sum - a[i])
            sum = 1
        elif sum + a[i] >= 0 and flag == True:
            flag = False
            count += abs(-1 - sum - a[i])
            sum = -1
        elif sum + a[i] > 0 and flag == False:
            sum += a[i]
            flag = True
            continue

    return count

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]

    p = first_positive(n,a)
    n = first_negative(n,a)

    if p < n:
        print(p)
    else:
        print(n)
