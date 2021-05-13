def execute(N, L):
    c = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if judge(L[i], L[j], L[k]):
                    c += 1

    return c

def judge(a, b, c):
    if a==b or b==c or c==a:
        return False
    if a+b > c and b+c > a and a+c >b:
        return True
    else:
        return False

if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))

    print(execute(N, L))