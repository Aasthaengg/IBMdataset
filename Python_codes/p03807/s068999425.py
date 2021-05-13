def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    odd  = 0
    for a in A:
        if a % 2 == 1:
            odd += 1

    if odd % 2 == 0:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    main()