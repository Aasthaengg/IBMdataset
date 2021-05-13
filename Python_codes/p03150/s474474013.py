import re
m = re.match(r'^keyence$|^.*keyence$|^k.*eyence$|^ke.*yence$|^key.*ence$|^keye.*nce$|^keyen.*ce$|^keyenc(\D)+e$|^keyence.*$',input())
print('YES' if m else 'NO')
