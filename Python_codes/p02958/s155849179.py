import numpy as np

N = int(input())
p_array = np.array(list(map(int, input().split())))

sorted_p = np.sort(np.copy(p_array))
diff = (p_array != sorted_p).sum()

if diff == 0:
    print('YES')
elif diff == 2:
    print('YES')
else:
    print('NO')