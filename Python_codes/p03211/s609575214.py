import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():

    S =input()
    prime =753
    ans =1000
    for i in range(len(S)-2):
        ans =min(ans, abs(prime-int(S[i:i+3])))

    print(ans)





if __name__ == "__main__":
    main()
