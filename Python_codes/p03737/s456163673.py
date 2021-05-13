def main():
    s1, s2, s3 = input().split()
    ans = '{}{}{}'.format(s1.upper()[0], s2.upper()[0], s3.upper()[0])
    print(ans)


if __name__ == "__main__":
    main()
