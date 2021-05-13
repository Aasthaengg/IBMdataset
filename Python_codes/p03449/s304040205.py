def main():
    n = int(input())
    a1lis = list(map(int, input().split()))
    a2lis = list(map(int, input().split()))

    a1sum = sum(a1lis)
    a2sum = sum(a2lis)

    tmp = a1lis[0]

    #i = 0
    total = a1lis[0] + a2sum
    ans = total

    for i in range(1, n):
        tmp += a1lis[i]
        a2sum -= a2lis[i-1]
        total = tmp + a2sum
        if total > ans:
            ans = total
    
    print(ans)

        
    



    

if __name__ == "__main__":
    main()