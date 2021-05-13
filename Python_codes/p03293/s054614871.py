import sys
S = input()
T = input()

sys.exit() if not (S.islower() or T.islower()) else ''
sys.exit() if not (2 <= len(S) <= 100) else ''

array_S = list(S)
array_T = list(T)

for I in range(len(array_S)):
    array_S.insert(0,array_S.pop(-1))
    if array_S == array_T:
        print('Yes')
        sys.exit()
print('No')