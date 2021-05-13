def main():
    P, Q, R = (int(x) for x in input().split())
    print(min(P + Q, Q + R, R + P))


if __name__ == "__main__":
    main()
