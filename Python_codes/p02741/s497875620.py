def main():
    sequence =list(map(int, "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51".split(', ')))
    kth = int(input())
    print(sequence[kth - 1])
       

main()