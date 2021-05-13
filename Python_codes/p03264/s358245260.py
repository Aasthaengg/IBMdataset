def main():
    K = int(input())
    odd = 0
    even = 0

    for i in range(K):
        if (i + 1) % 2 == 0:
            even += 1
        else:
            odd += 1
    
    print(even * odd)
main()