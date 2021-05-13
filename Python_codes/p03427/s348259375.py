N = int(input())
ketasu = len(str(N))
saijoui = int(str(N)[0])
if int(str(saijoui)+"9"*(ketasu-1)) > N:
    print(saijoui + 9*(ketasu-1)-1)
else:
    print(saijoui + 9*(ketasu-1) )
