import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    B_list = list(map(int, input().split()))

    if n == 2:
        sum_a0_a1 = B_list[0]*2
        print(sum_a0_a1)
        return

    first_a = B_list[0]
    last_a = B_list[n-2]
    sum_other_a = 0

    for i in reversed(range(0,n-2)):
        min_b = min(B_list[i+1],B_list[i])
        sum_other_a += min_b

    print(first_a + last_a + sum_other_a)


if __name__ == '__main__':
    main()