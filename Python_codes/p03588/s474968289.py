def main():
    N = int(input())
    A =[]
    B =[]
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse = True)
    #print(A,B)
    #１を求めるよ
    ans = 0
    ans += len(A)
    for i in range(len(A)-1):
        ans += A[i+1] - A[i] - 1
    #3を求めるよ
    ans += B[len(A)-1]
    #2を求めるよ
    tmp = A[0]-1
    #if B[0]+tmp > 1000000000:
        #ans += 1000000000 - B[0]
    #else:
    ans += tmp

    return ans

print(main())
