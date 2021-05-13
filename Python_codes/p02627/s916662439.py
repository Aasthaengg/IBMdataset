def ooMojiKomoji(chara):
    ret = False
    if str.isupper(chara) == True:
        ret = True
    return ret

a = str(input())

if ooMojiKomoji(a):
    print('A')
else:
    print('a')
