N=int(input())
a = [int(input()) for i in range(N)]
#はじめに奇数があったらfirstの勝ち
print('first' if 1 in [x%2 for x in a] else 'second')