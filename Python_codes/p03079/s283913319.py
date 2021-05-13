def main():

    A, B, C = map(int, input().split())
    if A == B == C:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(main())