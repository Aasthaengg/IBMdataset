def main():
    n = map(int, input().split())
    inlis = list(map(int, input().split()))

    tmp = 0
    for i in range(len(inlis)):
        tmp += 1/inlis[i]
    print(1/tmp)
    
    
if __name__ == "__main__":
    main()
