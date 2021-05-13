N = int(input())
L = sorted( list( map(int, input().split() ) ) )
print('Yes') if sum(L) > 2*L[N-1] else print("No")