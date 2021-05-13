N = int(input())

if N==0:
    print(0)
else:
    answer=[]
    while N != 0:

        if N % (-2) == 0:
            N=N//(-2)
            answer.append(0)
        else:
            N=N//(-2)+1
            answer.append(1)

    print(''.join(list(map(str, reversed(answer)))))
