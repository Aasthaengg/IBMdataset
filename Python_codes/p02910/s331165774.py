from sys import exit

S = input()
odd = set(['L','U','D'])
even = set(['R','U','D'])

for i in range(len(S)):
    if i%2 == 0:
        if S[i] not in even:
            print("No")
            exit(0)
    else:
        if S[i] not in odd:
            print("No")
            exit(0)

print("Yes")