A, B = map(int,input().split())
print('IMPOSSIBLE' if (A+B)&1 else int((A+B)/2))