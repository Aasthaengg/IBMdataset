import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    result = 0
    for i in range(n):
        current_b = B_list[i]
        rest_b = current_b - A_list[i]
        if rest_b > 0:
            result += A_list[i]
            rest_next_a = A_list[i+1] - rest_b
            if rest_next_a > 0:
                result += rest_b
                A_list[i+1] = rest_next_a
            else:
                result += A_list[i+1]
                A_list[i+1] = 0

        else:
            result += current_b

    print(result)


if __name__ == '__main__':
    main()