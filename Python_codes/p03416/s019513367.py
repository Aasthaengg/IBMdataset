A, B = map(int, input().split())
c = 0
for i in range(A, B+1):
    c += int(str(i)[::-1] == str(i))
print(c)
