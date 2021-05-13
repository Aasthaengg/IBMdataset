A, B, C = map(int, input().split())

print('Yes') if len({A, B, C}) == 2 else print('No')