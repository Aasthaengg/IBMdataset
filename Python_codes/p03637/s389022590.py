n = int(input())
aaa = list(map(int, input().split()))
odd = 0
even = 0
even4 = 0
for a in aaa:
    if a % 4 == 0:
        even4 += 1
    elif a % 2 == 0:
        even += 1
    else:
        odd += 1
if odd == 0:
    print('Yes')
else:
    if even4 == 0:
        print('No')
    else:
        if even == 0:
            print('Yes' if even4 >= odd - 1 else 'No')
        else:
            print('Yes' if even4 >= odd else 'No')