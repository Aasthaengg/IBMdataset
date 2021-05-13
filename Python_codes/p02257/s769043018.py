def is_prime(x) :
    if x == 2 :
        return True
    if x < 2 or x % 2 == 0 :
        return False

    return pow(2, x-1, x) == 1

def main() :
    n = int(input())
    nums = []
    for _ in range(n) :
        x = int(input())
        nums.append(x)

    count = 0
    for num in nums :
        if is_prime(num) :
            count += 1

    print(count)

if __name__ == '__main__' :
    main()