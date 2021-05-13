def main():
    import math
    n = int(input())
    inlis = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if inlis[i-1] < inlis[i] and inlis[i] < inlis[i+1]:
            ans += 1
        if inlis[i-1] > inlis[i] and inlis[i] > inlis[i+1]:
            ans += 1
    print(ans)
        

    
if __name__ == "__main__":
    main()
