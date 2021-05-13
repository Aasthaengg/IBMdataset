N = input()
print(max(sum([int(i) for i in N]),(len(N)-1)*9+int(N[0])-1))