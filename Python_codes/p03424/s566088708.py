n = int(input())
l = list(input().split())
if len(set(l)) == 4:
    print('Four')
else:
    print('Three')