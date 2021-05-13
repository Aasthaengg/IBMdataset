# -*- coding: utf-8 -*-

def main():

    A, B, C = map(int, input().split())

    if A == B and A != C or A == C and A != B or B == C and A != B:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()