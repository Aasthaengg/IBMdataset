s = input()
alpha = [0]*26
l = []
l.append('KIHBR')
l.append('AKIHBR')
l.append('KIHABR')
l.append('KIHBAR')
l.append('KIHBRA')

l.append('AKIHABR')
l.append('AKIHBAR')
l.append('AKIHBRA')
l.append('KIHABAR')
l.append('KIHABRA')
l.append('KIHBARA')
l.append('AKIHABAR')
l.append('KIHABARA')
l.append('AKIHBARA')
l.append('AKIHABRA')
l.append('AKIHABARA')
if s in l:
    print("YES")
else:
    print("NO")


