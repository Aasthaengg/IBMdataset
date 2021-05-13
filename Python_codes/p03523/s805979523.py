s=input()
if len(s)>9 or len(s)<5:
    print('NO')
    exit()
a=['AKIHABARA','KIHABARA','KIHBARA','KIHBAR','KIHBRA','KIHABAR','KIHABRA','KIHABR','KIHBR','AKIHBARA','AKIHBRA','AKIHBR','AKIHBAR','AKIHABRA','AKIHABR','AKIHABAR']
if s in a:
    print('YES')
else:
    print('NO')