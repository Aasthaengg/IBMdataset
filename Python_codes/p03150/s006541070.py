import re
m = re.match(r'^keyence$|^(\D+)keyence$|^k(\D+)eyence$|^ke(\D+)yence$|^key(\D+)ence$|^keye(\D+)nce$|^keyen(\D+)ce$|^keyenc(\D)+e$|^keyence(\D+)$',input())
print('YES' if m else 'NO')