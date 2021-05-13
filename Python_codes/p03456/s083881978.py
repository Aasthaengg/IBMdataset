import math
a, b = map(int, input().split())

n = int(str(a) + str(b))
# found = False
# for i in range(1, 330):
#     if(n == i**2):
#         # print(i)
#         found = True

# if(found == True):
#     print("Yes")
# else:
#     print("No")

if(math.floor(math.sqrt(n)) ** 2 == n):
    print("Yes")
else:
    print("No")
