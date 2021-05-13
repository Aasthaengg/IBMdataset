import functools

if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    a = functools.reduce(lambda x, y: x ^ y, A, 0)
    if a == 0:
        print("Yes")
    else:
        print("No")