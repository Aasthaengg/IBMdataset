def main():
    N = int(input())
    A = list(map(int, input().split()))

    scarf_0 = 0
    for a in A[1:]:
        scarf_0 ^= a
    
    scarf_all = scarf_0 ^ A[0]
    
    ans = [scarf_all^a for a in A]
    
    print(*ans, sep=" ")

if __name__ == "__main__":
    main()