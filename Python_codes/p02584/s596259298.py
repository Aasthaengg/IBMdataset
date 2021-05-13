x, k, d = map(int, input().split(' '))
b = x + k * d;
if b > 0:
    a = int(b / (2 * d))
    if a <= k:
        print(min(b-a*2*d, -(b-(a+1)*2*d)))
    else:
        print(b-k*2*d)
else:
    print(-b)