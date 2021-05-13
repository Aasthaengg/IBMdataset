def main():
    N = str(input())
    B_count = 0
    result = 0
    for i in range(0, len(N)):
        target = N[i]
        if target == 'W':
            result = result + B_count
        else:
            B_count = B_count + 1        
    print(result)

if __name__ == "__main__":
    main()