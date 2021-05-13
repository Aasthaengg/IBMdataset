if __name__ == '__main__':
    n =int(input())
    k =int(input())
    count =1

    for i in range(n):
        if count > k:
            count +=k
        else:
            count =count*2

    print(count)