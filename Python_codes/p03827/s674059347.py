N = int(input())
str1 = input()
li = list(str1)
a = 0
ma = 0
for i in range(N):
    if li[i] == 'I':
        a += 1
        ma = max(a,ma)
    else:
        a -= 1
print(ma)