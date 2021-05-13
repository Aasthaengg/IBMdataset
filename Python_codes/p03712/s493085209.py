H, W = map(int, input().split())
A = ['#' + input() + '#' for _ in range(H)]
A = ['#' * (W + 2)] + A + ['#' * (W + 2)]
print(*A, sep='\n')