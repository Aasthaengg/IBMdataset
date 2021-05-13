def main():
    n = int(input())
    k = int(input())
    #k > 2*n 2倍
    tmp = 1
    i=0
    while(i<n):
        if(tmp < k):
            tmp += tmp
        else:
            tmp += k
        i+=1
    print(tmp)
if __name__ == '__main__':
    main()
