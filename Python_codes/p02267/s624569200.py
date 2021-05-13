def main():
    _ = input()
    array_A = input().split()
    _ = input()
    array_B = input().split()

    array_intersection = set(array_A) & set(array_B)

    print(len(array_intersection))

    return


main()
