if __name__ == '__main__':
    n = int(input())
    d,x = map(int, input().split())
    count = x

    for i in  range(n):
        a = int(input())
        count+=1+((d-1)//a)

    print(count)