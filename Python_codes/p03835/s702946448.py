if __name__ == '__main__':
    b, c = map(int, input().split())
    num = b*3 -c

    count = 0
    for i in range (0,b+1):
        for j in range(0,b+1):
            if c-(i+j)<=b and c-(i+j) >=0:
                count+=1
    print(count)

