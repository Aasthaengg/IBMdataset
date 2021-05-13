if __name__ == "__main__":
    A, B = list(map(int, input().split()))
    num_of_tap = 0
    num_of_hole = 1
    while(num_of_hole < B):
        num_of_tap += 1
        num_of_hole = (A-1)*(num_of_tap-1) + A

    print(num_of_tap)