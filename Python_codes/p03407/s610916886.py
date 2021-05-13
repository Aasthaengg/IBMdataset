def main(A: int, B: int, C: int):
    if (A + B) >= C:
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    A, B, C = map(int, input().split(' '))

    print(main(A, B, C))
