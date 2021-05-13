s=input()
t,u=0<int(s[:2])<13,0<int(s[2:])<13
print('AMBIGUOUS' if t and u else 'MMYY' if t else 'YYMM' if u else 'NA')
