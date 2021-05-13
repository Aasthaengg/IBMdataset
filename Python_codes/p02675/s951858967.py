def solve():
    N = input()
    least_digit = int(N[-1])
    if least_digit in set([2,4,5,7,9]):
        print("hon")
    elif least_digit in set([0,1,6,8]):
        print("pon")
    else:
        print("bon")

if __name__ == "__main__":
    solve()