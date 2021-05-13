def main():
    X = int(input())
    if X <= 3:
        print(1)
        return
    
    ans = 0
    for n in range(2, X):
        p = 2
        while pow(n, p) <= X:
            if ans < pow(n, p):
                ans = pow(n, p)
            p += 1
    print(ans)
    
main()  