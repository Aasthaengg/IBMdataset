def main():

    S = input()
    T = "CODEFESTIVAL2016"
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    return ans



if __name__ == '__main__':
    print(main())