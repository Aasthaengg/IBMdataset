k=int(input())
A, B = map(int, input().split())

print('OK' if A<=(B-B%k) else 'NG')