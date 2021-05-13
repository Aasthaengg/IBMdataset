if __name__ == "__main__":
    a, b, x = [int(x) for x in input().split(" ")]
    print(((b // x) + 1 - (((a - 1) // x) + 1)))
