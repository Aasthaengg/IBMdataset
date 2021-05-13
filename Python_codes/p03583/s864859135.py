def main():
    n=int(input())
    for i in range(1,3501):
        for j in range(1,3501):
            if 4*i*j-n*i-n*j>0 and (n*i*j)%(4*i*j-n*i-n*j)==0:
                print(i,j, (n*i*j)//(4*i*j-n*i-n*j))
                return
if __name__ == "__main__":
    main()