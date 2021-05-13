N, A, B = map(int, input().split())
print(max(B*(N-2)-A*(N-2)+1, 0))