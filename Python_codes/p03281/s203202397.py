def is_target(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 8:
        return True
    else:
        return False

if __name__ == "__main__":
    N = int(input())
    count = 0
    for num in range(1, N+1, 2):
        count += is_target(num)

    print(count)