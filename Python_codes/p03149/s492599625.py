def main():
    ls = [int(x) for x in input().split()]
    ls.sort()
    ans = [1,4,7,9]
    for i in range(4):
        if ls[i]!=ans[i]:
            print("NO")
            exit()
    print("YES")
if __name__ == '__main__':
    main()