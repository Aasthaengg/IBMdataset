N = list(input())
num = len(N)
if N.count('9') == num:
    print(9*num)
elif N.count('9') == num-1 and N[0] != '9':
    print(int(N[0])+9*(num-1))
else:
    if num <= 1:
        print(''.join(N))
    else:
        ans = int(N[0])-1
        ans += 9*(num-1)
        print(ans)