N, A = map(int, open(0).read().split())
R = N%500
if (R <= A):
    print('Yes')
else:
    print('No')
