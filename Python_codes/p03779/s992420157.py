def main():
    x = int(input())
    jump_sum = 0
    for i in range(1, x+1):
        jump_sum += i
        if jump_sum >= x:
            break
    print(i)


if __name__ == "__main__":
    main()
