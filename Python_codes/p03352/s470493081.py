# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    x = int(input().rstrip())

    num_set = set()
    for i in range(1, x+1):
        num = i * i
        while num <= x and i not in num_set:
            num_set.add(num)
            num = num * i

    print(max(num_set))

if __name__ == "__main__":
    resolve()
