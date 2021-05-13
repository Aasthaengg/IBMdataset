def main():
    N = int(input())
    A = list(map(int,input().split()))
    i = 0
    j = 1
    money = 1000
    num_of_stock = 0

    while (i<N-1):
        #print(i)
        if A[i] < A[i+1]:
            num_of_stock += money // A[i]
            money = money % A[i]
        elif A[i] > A[i+1]:
            money += A[i]*num_of_stock
            num_of_stock = 0
        else:
            i += 1
            continue
        i += 1

    money += A[N-1]*num_of_stock

    return money

print(main())
