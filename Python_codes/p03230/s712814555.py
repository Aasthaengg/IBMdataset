
def resolve():
    N = int(input())
    
    K = 0
    for i in range(1, 1000):
        if (i*(i-1)//2 == N):
            K = i
            break

    if K == 0:
        print("No")
        return
    else:
        S = [[] for _ in range(K)]
        cnt = 1
        for i in range(K):
            for j in range(i+1, K):
                S[i].append(cnt)
                S[j].append(cnt)
                cnt += 1

    print("Yes")
    print(K)
    for s in S:
        print(len(s), *s)

if __name__ == "__main__":
    resolve()