H, W = map(int, input().split())
ans  = ['#'*(W+2)] + ['#'+input()+'#' for i in range(H)] + ['#'*(W+2)]
print(*ans, sep='\n')