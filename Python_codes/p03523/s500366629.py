def bi(x):
    o = [0]*4
    for i in range(4):
        o[i] = ['A',''][x % 2]
        x //= 2
    return o

S = input()
for i in range(64):
    o = bi(i)
    if S == ''.join([o[0],'KIH',o[1],'B',o[2],'R',o[3]]):
        print("YES")
        exit()

print("NO")