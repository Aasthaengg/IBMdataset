s = input() + 'C'
t = s[::-1] + 'F'

# CF
# 最も左にある C 
# 最も右にある F

idx_C = s.index('C')
idx_F = len(s) - 1 - t.index('F')

if idx_C < idx_F:
    print('Yes')
else:
    print('No')