N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
jdg = False
if max(x) < min(y):
    if min(y)>X and max(x)<Y:jdg=True

print('No War' if jdg else 'War')