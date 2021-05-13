N = list(map(int,input().split()))
print('YES' if all([True if i in N else False for i in [1,4,9,7]]) else 'NO')