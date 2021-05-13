import sys
O = str(input())
E = str(input())
# print(O)
# print(E)
O_array = list(O)
E_array = list(E)
# print(O_array)
# print(E_array)
if not O.islower() or not E.islower():
    sys.exit()
if len(O) < 0 or len(O) > 50 or len(E) < 0 or len(E) > 50:
    sys.exit()
diff_length = len(O) - len(E)
if not (diff_length == 0 or diff_length == 1):
    sys.exit()

for e in range(len(E)):
    print(O[e], end='')
    print(E[e], end='')
if diff_length == 1:
    print(O[-1])
else:
    print('')