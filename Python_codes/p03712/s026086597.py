h,w = map(int, input().split())
r = ['#'*(w+2)]
a = r + ['#'+input()+'#' for _ in range(h)] + r
for s in a: print(s)
