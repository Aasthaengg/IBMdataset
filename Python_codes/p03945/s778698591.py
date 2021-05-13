def main():
    S  = input()
    A = S[0]

    for i in range(len(S)):
        if(S[i]!=A[len(A)-1]):
            A = A + S[i]

    print(len(A)-1)



if __name__ == '__main__':
    main()
