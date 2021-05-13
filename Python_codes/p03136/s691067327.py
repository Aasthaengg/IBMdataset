N = int(input())
L = sorted(list(map(int, input().split())))

print('Yes' if(sum(L[:-1])-L[-1] > 0) else 'No')
