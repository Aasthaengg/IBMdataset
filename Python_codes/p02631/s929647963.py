def main():
    N = int(input())
    a = list(map(int, input().split()))
 
    total = 0
    for other in a:
        total ^= other
 
    print(*[(other ^ total) for other in a])
 
 
if __name__ == "__main__":
    main()