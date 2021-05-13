N = input()
if N[1:] == (len(N)-1)*'9':
    print(int(N[0]) + (len(N)-1)*9)
else:
    print((int(N[0])-1) + (len(N)-1)*9)
