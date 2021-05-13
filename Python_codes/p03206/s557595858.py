def aChristmas(d):

    ans = "Christmas"
    for i in range(abs(25-d)):
        ans += " Eve"
    return ans

def main():
    d = int(input())
    print(aChristmas(d))

if __name__ == '__main__':
    main()