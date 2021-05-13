def main():
    num_max, length, d = [int(_) for _ in input().split()]

    d_pattern = num_max - d if d == 0 else (num_max - d) * 2
    prob = d_pattern / (num_max ** 2)

    print(prob * (length - 1))

main()
