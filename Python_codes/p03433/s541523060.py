N = int(input())
A = int(input())

nokori = N %500
if nokori>A:
    print('No')
else:
    print('Yes')