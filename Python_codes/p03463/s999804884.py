# A - Move and Win

N, A, B = map(int, input().split())
ans = ['Alice', 'Borys']
print(ans[(B-A)%2])