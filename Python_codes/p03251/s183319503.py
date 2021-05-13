N, M, X, Y = map(int, input().split())
XL = list(map(int, input().split())) + [X]
YL = list(map(int, input().split())) + [Y]
XL.sort()
YL.sort(reverse=True)
xt = XL.pop()
yt = YL.pop()
if xt < yt:
    print('No War')
else:
    print('War')
