def FactorialMod(N,Mod):
    if N>=Mod:
        return 0
    else:
        FactM = 1
        for TF in range(1,N+1):
            FactM = (FactM*TF)%Mod
        return FactM
print(FactorialMod(int(input()),10**9+7))