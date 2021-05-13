s = input()
ok = False

if s.startswith('keyence'):
    ok = True
if s.startswith('k') and s.endswith('eyence'):
    ok = True
if s.startswith('ke') and s.endswith('yence'):
    ok = True
if s.startswith('key') and s.endswith('ence'):
    ok = True
if s.startswith('keye') and s.endswith('nce'):
    ok = True
if s.startswith('keyen') and s.endswith('ce'):
    ok = True
if s.startswith('keyenc') and s.endswith('e'):
    ok = True
if s.endswith('keyence'):
    ok = True

if ok:
    print('YES')
else:
    print('NO')