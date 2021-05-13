A,B,C = (int(T) for T in input().split())
Flag = False
for T in range(1,B+1):
    if (T*A)%B==C:
        Flag = True
print(['NO','YES'][Flag])