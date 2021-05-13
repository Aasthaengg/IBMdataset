import re
s = input()
pattern={
    '.*keyence'
    ,'k.*eyence'
    ,'ke.*yence'
    ,'key.*ence'
    ,'keye.*nce'
    ,'keyen.*ce'
    ,'keyenc.*e'
    ,'keyence.*'
    }

for p in pattern:
    if re.fullmatch(p, s):
        print('YES')
        break
else:
    print('NO')