N = int(input())
S = list(map(str,input().split()))
if len(set(S)) == 4:
    print('Four')
elif len(set(S)) == 3:
    print('Three')