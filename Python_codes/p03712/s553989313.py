h, w = map(int,input().split())
image = [['#'*(w+2)]]
for _ in range(h):
    image.append(['#' + input() + '#'])
image.append(['#'*(w+2)])


for v in image:
    print(*v)