A, B = map(int, input().split())
print(sum(str(i) == str(i)[::-1] for i in range(A, B + 1)))