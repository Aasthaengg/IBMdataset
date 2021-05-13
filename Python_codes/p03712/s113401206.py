
H,W = map(int,input().split())
st = ['#' + str(input()) +'#' for _ in range(H)]
st = ['#'*(W+2)] + st + ['#'*(W+2)]
print(*st,sep='\n')