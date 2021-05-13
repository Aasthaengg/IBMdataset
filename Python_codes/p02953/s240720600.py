def main():
    N = int(input())
    A = list(map(int,input().split()))
    pre = A[0]
    for i in A:
        if pre > i:
            print("No")
            return
        elif pre < i:
            pre = i -1
    print("Yes")        
if __name__ == "__main__":
    main()     