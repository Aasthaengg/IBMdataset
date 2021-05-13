import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    s=str(input())
    if s in ['AKIHABARA','AKIHABAR','AKIHABRA','AKIHABR','AKIHBARA','AKIHBARA','AKIHBRA','AKIHBR','KIHABARA','KIHABAR','KIHABRA','KIHABR','KIHBARA','KIHBAR','KIHBRA','KIHBR']:
        print('YES')
    else:
        print('NO')

resolve()
