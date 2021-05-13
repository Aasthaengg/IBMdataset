import re
s = input()
t = ['KIHBR','AKIHBR','KIHABR','KIHBAR','KIHBRA','AKIHABR','AKIHBAR','AKIHBRA','KIHABAR','KIHABRA','KIHBARA','AKIHABAR','AKIHABRA','AKIHBARA','AKIHABARA']

if s in t:
    print('YES')
else:
    print('NO')