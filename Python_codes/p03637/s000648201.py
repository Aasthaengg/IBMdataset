n = int(input())
l = list(map(int, input().split()))

even = len([i for i in l if i % 2 == 0])
four = len([i for i in l if i % 4 == 0])
even_wo_four = even - four

if four >= n//2:
    print('Yes')
elif n - four * 2 == even_wo_four:
    print('Yes')
else:
    print('No')