N, A, B = map(int, input().split())
diff = B-A

if diff%2 ==0:
    print('Alice')
elif diff%2 !=0:
    print('Borys')
else:
    print('Draw')