def main():
    nums = map(int, raw_input().split())
    print gcd(nums[0], nums[1])

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

main()