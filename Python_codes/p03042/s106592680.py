s=input();a,b=map(int,(s[:2],s[2:]));print('AMBIGUOUS'if 1<=a<=12 and 1<=b<=12 else'MMYY'if 1<=a<=12 and 0<=b<=99 else'YYMM'if 0<=a<=99 and 1<=b<=12 else'NA')