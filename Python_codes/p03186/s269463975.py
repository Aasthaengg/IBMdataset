#AGC030 A
'''
問題:
解毒剤入りの美味しくないクッキーがA枚ある
解毒剤入りの美味しいクッキーがB枚ある
毒入りの美味しいクッキーがC枚ある

毒入りのクッキーを食べるとお腹を壊す
お腹を壊した状態では毒入りのクッキーを食べることはできない
お腹を壊した状態で解毒剤入りのクッキーを食べるとお腹が治る

美味しいクッキーは最大で何枚食べられるか?

考察:
毒入りの美味しいクッキーはA+B+1枚まで食べることができる
'''

A,B,C = map(int,input().split(' '))

print(str(min(A+B+1, C)+B))