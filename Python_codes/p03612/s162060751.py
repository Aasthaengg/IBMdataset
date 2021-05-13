def main():
    n = int(input())
    inlis= list(map(int, input().split()))
    ans = 0

    for i in range(n-1, -1, -1):
        #print(i)
        if inlis[i] != i+1:
            #print(i, inlis[i], i+1)
            break
        else:
            #print(inlis)
            #print("mae", inlis[i])
            if i-1 >= 0:
                a = inlis[i-1]
                inlis[i] = a
                inlis[i-1] = i+1
                ans += 1
                #print(inlis)
                
    if ans < n-1:
        #print(inlis)
        for i in range(n):
            if inlis[i] == i+1 and i+1 <= n-1:
                #print("ato", inlis[i])
                b = inlis[i+1]
                inlis[i] = b
                inlis[i+1] = i
                ans += 1
        
    print(ans)


    
if __name__ == "__main__":
    main()
