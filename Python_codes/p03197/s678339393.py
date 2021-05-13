print("second" if all(i % 2 == 0 for i in map(
    int, open(0).read().split()[1:])) else "first")