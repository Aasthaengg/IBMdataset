def main():
    n = int(input())

    n1 = list(map(int,input().split()))

    if 0 in n1:
        print(0)
        return

    sum = 1
    for i in n1:
        sum *= i
        if sum > 1000000000000000000:
            print(-1) 
            return 
    print(sum)

main()