import sys
def main():
    input = sys.stdin.readline
    N,T=map(int, input().split())
    *A,=map(int, input().split())
    R=[]
    mn=(A[0],set([0]))
    for i in range(1,N):
        if A[i] > mn[0]:
            R.append((A[i] - mn[0], mn[1]))
        elif mn[0] == A[i]:
            mn[1].add(i)
        else:
            mn = (A[i],set([i]))
    R.sort(reverse=True, key=lambda x:x[0])
    ans = 0
    mx = R[0][0]
    tmp1 = set()
    cnt = 0
    for r in R:
        if r[0] != mx: break
        cnt += 1
        tmp1 |= r[1]
    print(min(cnt, len(tmp1)))

if __name__ == '__main__':
    main()