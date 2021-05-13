import math
def main():
    Dog, Mon = map(int, input().split())
    comb = 0

    if Dog > Mon:
        if Dog > Mon + 1:
            pass
        else:
            comb = (math.factorial(Dog) * math.factorial(Mon)) % (10**9+7)

    elif Dog == Mon:
        comb = (math.factorial(Dog) * math.factorial(Mon) * 2) % (10**9+7)
    else:
        if Mon -1 > Dog:
            pass
        else:
            comb = (math.factorial(Dog) * math.factorial(Mon)) % (10**9+7)

    print(comb)

if __name__ == "__main__":
    main()