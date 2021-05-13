def main():
    import math
    n, m = map(int, input().split())
    if n - m <= -2 or n - m >= 2:
        print(0)
        exit()

    else:
        if n != m:
            ans = math.factorial(n) % (10**9 + 7) * math.factorial(m) % (10**9 + 7)
        else:
            ans = math.factorial(n) * 2 % (10**9 + 7) * math.factorial(m) % (10**9 + 7)

    print(ans)


    

 
    
    
if __name__ == "__main__":
    main()