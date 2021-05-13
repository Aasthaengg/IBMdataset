

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    a = sorted([int(i) for i in input().split()], reverse=True)

    bob = 0
    alice = 0
    for m in range(len(a)):
        if m % 2 == 0:
            alice += int(a[m])
        else:
            bob += int(a[m])

    print(alice - bob)
