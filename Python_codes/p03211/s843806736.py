s = list(input())
# print(''.join(s[0:3]))
A = []
for i in range(0, len(s) - 2):
    A.append(abs(int(''.join(s[i:i+3])) - 753))
# for i in range(0, len(s) - 4):
#     A.append(abs(int(''.join(s[i:i+4])) - 753))
print(min(A))
