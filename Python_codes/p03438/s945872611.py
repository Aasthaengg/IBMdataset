def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    need = 0
    stock = 0
    for a, b in zip(A, B):
        if a > b: need += (a-b)
        if b > a: stock += (b-a)//2

    if stock >= need:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()