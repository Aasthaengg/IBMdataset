N = int(input())
a = list(map(int, input().split()))

a_4 = [val for val in a if val % 4 == 0]
num_4=len(a_4)
a_odd = [val for val in a if val % 2 ==1]
num_odd=len(a_odd)
num_2 = N - num_odd - num_4


if num_odd==0:
    print('Yes')
else:
    if 1<=num_odd<=num_4:
        print('Yes')
    elif num_4+1==num_odd:
        if num_2==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')