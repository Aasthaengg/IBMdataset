def main():
    S = input()
    k = int(input())

    array = []
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            if j-i <= k:
                array.append(S[i:j])
    array = list(set(array))
    array.sort()
    print(array[k-1])


if __name__ == '__main__':
    main()
