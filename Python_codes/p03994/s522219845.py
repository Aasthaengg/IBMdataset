#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))


def main():
    S = list(input())
    K = int(input())

    li = list("abcdefghijklmnopqrstuvwxyz")
    dic = {}
    for i,j in enumerate(li):
        dic[j] = 26-i
    dic["a"] = 0

    for i in range(len(S)):
        if dic[S[i]] <= K:
            K -= dic[S[i]]
            S[i] = "a"
    if K>0:
        num = (dic[S[-1]]-26)*(-1)
        S[-1] = li[(num+K)%26]

    for i in range(len(S)):
        print(S[i],end="")
    print()


if __name__ == "__main__":
    main()




