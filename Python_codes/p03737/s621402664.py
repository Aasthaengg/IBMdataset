# A - Three-letter acronym
def main():
    s1, s2, s3 = input().split()

    ans = s1[0]+s2[0]+s3[0]
    print(ans.upper())


if __name__ ==  "__main__":
    main()