def main():
    n = int(input())
    A = list(map(int,input().split()))
    q = int(input())
    m = list(map(int,input().split()))

    sum_list = []
    back = []
    #bit全探索
    for i in range(1,2**n):
        for j in range(n):
            if ( (i>>j)&1 ):
                back.append(A[j])

        #print(back)

        sum = 0
        for k in back:
            sum += k

        sum_list.append(sum)

        back = []

    for h in range(q):
        if m[h] in sum_list:
            print('yes')
        else:
            print('no')

main()

