def main():
    k,s=map(int, input().split())
    res=0
    for i in range(k+1):
        for j in range(k+1):
            if(s-(i+j)>=0 and s-(i+j)<=k):
                res+=1
    print(res)


if __name__ == '__main__':
    main()
