def TripleDots():

    Num = int(input())

    moji = str(input())

    if len(moji) > Num:
        moji_cut = moji[:Num] + '...'
        
    else:
        moji_cut = moji

    print(moji_cut)

if __name__ == '__main__':
    TripleDots()

