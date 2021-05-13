N = int(input())
S = list([x for x in input().split()])

result = set(S)

if len(result) == 4:
    print('Four')
else:
    print('Three')
