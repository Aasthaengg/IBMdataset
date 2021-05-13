n = int(input())
div = 0
for i in str(n):
    num = int(i)
    div += num

if div % 9 == 0:
    print("Yes")
else:
    print('No')