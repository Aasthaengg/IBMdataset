
a,b,c = map(int,input().split())

count = 0
for i in range(100):
    if a%2==1 or b%2==1 or c%2==1:
        break

    count = count + 1
    a_new = (b+c)/2
    b_new = (a + c) / 2
    c_new = (a + b) / 2

    a = a_new
    b = b_new
    c = c_new
    if i == 99:
        count = -1
print(count)