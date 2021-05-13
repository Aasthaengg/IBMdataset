import sys

input = sys.stdin.readline


def main():
    S = input().strip()
    K = int(input())

    dic = []
    for i in range(len(S)):
        j = 0
        tmp = ""
        while i + j < len(S) and j < 5:
            tmp += S[i + j]
            if tmp not in dic:
                dic.append(tmp)
            j += 1

    dic.sort()
    print(dic[K - 1])



    
    
    


if __name__ == '__main__':
    main()
