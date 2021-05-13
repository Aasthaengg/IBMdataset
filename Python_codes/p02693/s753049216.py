K = int(input())
A,B = map(int, input().split())

print('OK' if B//K - (A - 1)//K > 0 else 'NG')