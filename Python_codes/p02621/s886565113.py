def calc(a: int) -> int:
    return a+a**2+a**3

if __name__ == "__main__":
    a = int(input())
    print(calc(a))