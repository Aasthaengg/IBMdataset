s = sum(map(int,input().strip().split()))
print('IMPOSSIBLE' if s%2 else s//2)