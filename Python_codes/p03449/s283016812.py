# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline


    n = int(input().rstrip())
    a1_list = [int(x) for x in input().rstrip().split(" ")]
    a2_list = [int(x) for x in input().rstrip().split(" ")]


    upper_sum = a1_list[0]
    lower_sum = sum(a2_list)
    ans = upper_sum + lower_sum
    for i in range(1, n):
        upper_sum += a1_list[i]
        lower_sum -= a2_list[i-1]
        candy = upper_sum + lower_sum
        if candy > ans:
            ans = candy
    print(ans)




if __name__ == "__main__":
    resolve()
