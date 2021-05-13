def calc(N):
    n = 0
    for i in range(1,N+1):
        n+=i
        if n>=N:break
    if n!=N:
        print("No")
        return
    print("Yes")
    print(i+1)
    S = [list(range(1,i+1))]
    print(i,*S[0])
    m = i
    for j in range(1,i+1):
        S.append([])
        for s in S[:-1]:
            S[-1].append(s.pop())
        S[-1].extend(range(m+1,m+1+i-j))
        m = max(S[-1])
        print(i,*S[-1])
def main():
    N=int(input())
    calc(N)
main()