def func(A, B):
    ans = list({"1", "2", "3"} - {A, B})[0]
    return ans


if __name__ == "__main__":
    A, B = input(), input()
    print(func(A, B))
