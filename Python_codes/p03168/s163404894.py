N = int(input())
def main():
    head_prob_table = [[0.0] * (N+1) for i in range(N)]
    head_prob = list(map(float, input().split()))

    head_prob_table[0][1] = head_prob[0]
    head_prob_table[0][0] = 1-head_prob[0]

    for i in range(1, N):
        for j in range(i+2):
            head_prob_table[i][j] += head_prob_table[i-1][j] * (1 - head_prob[i])
            if j > 0:
                head_prob_table[i][j] += head_prob_table[i-1][j-1] * head_prob[i]

    print(sum(head_prob_table[N-1][(N+1)//2:]))

if __name__ == '__main__':
    main()