keys = input().split(' ')
vals = list(map(int, input().split(' ')))
hoge = input()
print(vals[0]-(keys[0]==hoge), vals[1]-(keys[1]==hoge))