N=int(input())
arrH=[int(i) for i in input().split()]

M=''.join(['C' if arrH[i]>=arrH[i+1] else ' ' for i in range(N-1)]).split()
print(0 if len(M)==0 else max([len(i) for i in M]))
