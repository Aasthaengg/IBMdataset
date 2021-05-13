N=int(input())
print(['No','Yes'][9 in [N%10, (N-N%10)//10]])
