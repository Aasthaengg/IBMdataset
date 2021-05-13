a,b,c,k = list(map(int, input().strip().split()))
if ((-1)**(k-1))*(a-b)<=10**18:
    print(((-1)**((k)%2))*(a-b))
else:
    print("Unfair")