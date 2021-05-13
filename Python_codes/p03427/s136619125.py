N=list(input())
if len(N) == 1:
    print(int(N[0]))
    exit()
all9 = True
for i in range(1,len(N)):
    if N[i] != '9':
        all9 = False
        break

c = int(N[0])
if not all9:
    c -= 1
print(c + 9 * (len(N)-1))
