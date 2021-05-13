n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
numa = 0
numb = 0
num = sum(b)-sum(a)
for i in range(n):
    x = b[i] - a[i]
    if x > 0:
        numa += -(-x//2)
        if x % 2 == 1:
            numb += 1
    else:
        numb -= x
if (num-numa)*2 == num-numb and num >= numa:
    print("Yes")
else:
    print("No")