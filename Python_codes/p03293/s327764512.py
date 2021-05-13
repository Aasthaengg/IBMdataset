s = input()
t = input()
#sを二回並べる
s += s
#sを二回並べた中にtがあれば、回転でいつかたどり着ける。
if(t in s):
    print('Yes')
else:
    print('No')
