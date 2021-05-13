h, w = map(int, input().split())

a = ['#' * (w+2)]
for _ in range(h):
    a.append('#' + input() + '#')
a.append('#' * (w+2))

for i in a:
    print(i)