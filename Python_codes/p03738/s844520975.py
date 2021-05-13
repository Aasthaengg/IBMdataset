import sys
A = input()
B = input()
if len(A) > len(B):
    print('GREATER')
    sys.exit()
elif len(A) < len(B):
    print('LESS')
    sys.exit()
elif A == B:
    print('EQUAL')
    sys.exit()

for i in range(len(A)):
    if A[i] == B[i]:
        i += 1
        continue
    elif A[i] > B[i]:
        print('GREATER')
        sys.exit()
    elif A[i] < B[i]:
        print('LESS')
        sys.exit()
print('EQUAL')