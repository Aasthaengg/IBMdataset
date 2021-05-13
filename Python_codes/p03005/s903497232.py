def input_func():
    N, K= map(int,input().split())
    return N, K

def evaluate(N,K):
    if K == 1:
        answer = 0
    else:
        answer = N - K
    return answer

if __name__ == '__main__':
    N, K = input_func()
    answer = evaluate(N,K)
    print(answer)