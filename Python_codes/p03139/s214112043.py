N, A, B = map(int, input().split())
print(str(min(A, B)) + " " + str(max(A + B - N, 0)))