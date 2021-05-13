import sys

S = input()
T = input()

changes = {}
changes_reverse = {}
for i in range(len(T)):
    #print(changes)
    if S[i] != T[i]:
        if S[i] in changes:
            if changes[S[i]] != T[i]:
                print('No')
                sys.exit(0)
        if T[i] in changes_reverse:
            if changes_reverse[T[i]] != S[i]:
                print('No')
                sys.exit(0)

        changes[S[i]] = T[i]
        changes_reverse[T[i]] = S[i]
    else:
        changes[S[i]] = T[i]
        changes_reverse[T[i]] = S[i]
        

print('Yes')
# print(changes)
