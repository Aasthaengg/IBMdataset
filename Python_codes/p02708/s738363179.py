def main():
    n, k = (int(i) for i in input().split())
    num_sums = sum((n-j+1)*j + 1 for j in range(k, n+2)) 
    print(num_sums % (10**9 + 7))

main()