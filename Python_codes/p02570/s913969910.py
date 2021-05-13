def main():
    D, T, S = map(int, input().split())
    speed = D / T
    if speed <= S:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()