def actual(H, W, A):
    answer = ''

    answer += '#' * (W + 2) + '\n'

    for a in A:
        answer += f'#{a}#\n'

    answer += '#' * (W + 2)

    return answer

H, W = map(int, input().split())
A = [input() for _ in range(H)]

print(actual(H, W, A))