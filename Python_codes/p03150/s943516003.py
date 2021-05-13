S=input()
if 'keyence'==S[:7] or 'keyence'==S[-7:]:
    print('YES')
    exit()
if 'k'==S[:1] and 'eyence'==S[-6:]:
    print('YES')
    exit()
if 'ke'==S[:2] and 'yence'==S[-5:]:
    print('YES')
    exit()
if 'key'==S[:3] and 'ence'==S[-4:]:
    print('YES')
    exit()
if 'keye'==S[:4] and 'nce'==S[-3:]:
    print('YES')
    exit()
if 'keyen'==S[:5] and 'ce'==S[-2:]:
    print('YES')
    exit()
if 'keyenc'==S[:6] and 'e'==S[-1:]:
    print('YES')
    exit()
print('NO')