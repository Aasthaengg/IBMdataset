

def main(numbers: list):
    a = int(numbers[0])
    b = int(numbers[1].replace('.', ''))
    ans = a * b // 100
    print(ans)


# N = int(input())
line = list(map(str, input().split()))
main(line)
