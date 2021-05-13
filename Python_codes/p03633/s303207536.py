def main():
    import fractions
    n = int(input())
    inlis = []
    for _ in range(n):
        a = int(input())
        inlis.append(a)
    
    ans = inlis[0]
    for i in range(1, n):
        ans = ans * inlis[i] // fractions.gcd(ans, inlis[i])

    print(ans)

    
    
if __name__ == "__main__":
    main()
