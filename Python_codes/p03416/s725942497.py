#B - Palindromic Numbers
A,B = map(int,input().split())
count = 0
for i in range(A,B+1):
    i = str(i)
    if i[0] == i[1] == i[3] == i[4] or (i[0] == i[4] and i[1] == i[3]):
        count += 1
print(count)