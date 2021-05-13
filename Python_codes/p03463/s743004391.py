'''
自身が動いて相手に接することができる側が勝つ
'''

N, A, B = map(int, input().split())

if abs(A - B) % 2 == 0:
    print("Alice")
else:
    print("Borys")