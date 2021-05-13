A,B = map(int,input().split())

count = 0
for i in range(A, B + 1):
    aa =str(i)
    rslt = aa[::-1]
    if aa == rslt:
        count += 1
print(count)