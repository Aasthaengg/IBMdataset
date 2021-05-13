import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if s in ['AKIHABARA','KIHABARA','AKIHBARA','AKIHABRA','AKIHABAR',\
             'KIHBARA','KIHABRA','KIHABAR','AKIHBRA','AKIHBAR','AKIHBRA',\
             'KIHBRA','KIHBAR','KIHABR','AKIHBR','KIHBR',]:
       print('YES')
    else:
        print('NO')
resolve()
