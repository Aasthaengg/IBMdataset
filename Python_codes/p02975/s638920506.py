def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    k = A[0]
    for i in A[1:]:
        k^=i
    if(k!=0):
        print("No")
    else:
        print("Yes")




if __name__ == '__main__':
    main()
