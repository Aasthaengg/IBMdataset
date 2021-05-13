S=str(input())
w=int(input())
print(''.join([S[i*w] for i in range(-(-len(S)//w))]))

