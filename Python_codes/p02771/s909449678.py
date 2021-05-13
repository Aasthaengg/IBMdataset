def main():

    A, B, C = map(int, input().split())
    if len(set([A, B, C])) == 2:
        return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())
